from datetime import datetime

from rest_framework import mixins, viewsets, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CategorySerializer, ArticleSerializer, ArchiveSerializer
from .serializers import CreateArticleSerializer, TagSerializer, ArticleProfileSerializer
from .models import Category, Article
from .filters import ArticleFilter
from utils.permissions import IsOwnerOrReadOnly

# Create your views here.


class ArticlePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 10


class CategoryViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    list: 文章分类列表页
    create: 创建一个文章类别
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAdminUser(), IsOwnerOrReadOnly()]
        return [IsOwnerOrReadOnly()]


class ArticleProfileViewSet(CacheResponseMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list: 文章简介列表
    """
    queryset = Article.objects.all().order_by('-update_time')
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = ArticleProfileSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    list: 文章列表
    create: 添加一个文章
    update: 更新一个文章
    delete: 删除一个文章
    retrieve: 文章详情
    """
    queryset = Article.objects.all().order_by('-update_time')
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    pagination_class = ArticlePagination

    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = ArticleFilter
    ordering_fields = ('update_time', 'like_nums')

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateArticleSerializer
        return ArticleSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAdminUser(), IsOwnerOrReadOnly()]
        return [IsOwnerOrReadOnly()]

    def retrieve(self, request, *args, **kwargs):
        # 重写查看详情逻辑，每次查看详情，该文章阅读数加1
        instance = self.get_object()
        instance.view_nums += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        # 重写更新逻辑，只有当文章内容发生改变时，才修改文章的更新时间
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if len(request.data['content']) != len(instance.content):
            instance.update_time = datetime.now()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class ArchiveViewSet(CacheResponseMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    文章归档
    """
    queryset = Article.objects.all()

    def list(self, request, *args, **kwargs):
        # 重写查看列表逻辑，返回由年份和月份组成的一个datetime类型的集合
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        time_list = []
        for i in queryset:
            time_list.append(str(i.update_time.year) + '-' + str(i.update_time.month))

        serializer = ArchiveSerializer([{'archive': datetime.strptime(i, '%Y-%m')} for i in set(time_list)], many=True)

        return Response(serializer.data)


class TagViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    文章Tag
    """
    queryset = Article.objects.all()

    def list(self, request, *args, **kwargs):
        # 重写查看列表逻辑，提取并返回所有文章的tag
        queryset = self.filter_queryset(self.get_queryset())

        tag_list = []
        for item in queryset:
            if item.tags is not None:
                tag_list += [i for i in item.tags.split(',')]

        serializer = TagSerializer([{'tag': i} for i in set(tag_list)], many=True)

        return Response(serializer.data)

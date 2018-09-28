from rest_framework import mixins, viewsets, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import CategorySerializer, ArticleSerializer
from .models import Category, Article
from utils.permissions import IsOwnerOrReadOnly

# Create your views here.


class CategoryViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    list: 文章分类列表页
    create: 创建一个文章类别
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    list: 文章列表
    create: 添加一个文章
    update: 更新一个文章
    delete: 删除一个文章
    retrieve: 文章详情
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAdminUser(), IsOwnerOrReadOnly()]
        return [IsOwnerOrReadOnly()]

from rest_framework import mixins, viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Fav, Comment, Reply, Like, Message, Dynamics
from .serializers import FavSerializer, CommentSerializer, CommentDetailSerializer, DynamicsSerializer
from .serializers import ReplySerializer, ReplyDetailSerializer, LikeSerializer, MessageSerializer
from utils.permissions import IsOwnerOrReadOnly, IsFromOrReadOnly


# Create your views here.


class FavViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                 mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    """
    list: 收藏列表
    create: 添加收藏
    delete: 取消收藏
    retrieve: 收藏详情
    """
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    serializer_class = FavSerializer

    def get_queryset(self):
        return Fav.objects.filter(user=self.request.user)


class LikeViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    """
    create: 点赞
    delete: 取消点赞
    """
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)


class CommentViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """
    list: 评论列表
    create: 添加评论
    delete: 删除评论
    retrieve: 评论详情
    """
    queryset = Comment.objects.all().order_by('-create_time')
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsOwnerOrReadOnly, )
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('article', )

    # 动态配置Serializer
    serializer_class = CommentDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReplyViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                   mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    """
    list: 回复列表
    create: 添加回复
    delete: 删除回复
    retrieve: 回复详情
    """
    queryset = Reply.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsFromOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('comment',)

    serializer_class = ReplyDetailSerializer

    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)


class MessageViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    list: 留言列表
    create: 添加留言
    """
    queryset = Message.objects.all().order_by('-create_time')
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = MessageSerializer


class DynamicsViewSet (mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list: 动态列表
    """
    queryset = Dynamics.objects.all().order_by('-create_time')
    serializer_class = DynamicsSerializer

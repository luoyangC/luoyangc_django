from rest_framework import mixins, viewsets, permissions

from .models import Fav, Comment, Reply
from .serializers import FavSerializer, CommentSerializer, CommentDetailSerializer, ReplySerializer
from utils.permissions import IsOwnerOrReadOnly

# Create your views here.


class FavViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    queryset = Fav.objects.all()
    serializer_class = FavSerializer


class CommentViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):

    queryset = Comment.objects.all()

    # 动态配置Serializer
    def get_serializer_class(self):
        if self.action == 'create':
            return CommentSerializer
        return CommentDetailSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        elif self.action == 'delete':
            return [IsOwnerOrReadOnly()]
        return []


class ReplyViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

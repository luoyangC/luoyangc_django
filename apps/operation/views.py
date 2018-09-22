from rest_framework import mixins, viewsets

from .models import Fav, Comment, Reply
from .serializers import FavSerializer, CommentSerializer, ReplySerializer
# Create your views here.


class FavViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Fav.objects.all()
    serializer_class = FavSerializer


class CommentViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReplyViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

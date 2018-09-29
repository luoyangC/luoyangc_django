"""
  Created by Amor on 2018-09-22
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Fav, Comment, Reply, Like
from users.serializers import UserDetailSerializer

__author__ = '骆杨'


User = get_user_model()


class FavSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Fav
        exclude = ('status', 'create_time')


class LikeSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Like
        exclude = ('status', 'create_time')


class ReplySerializer(serializers.ModelSerializer):

    from_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    like_nums = serializers.IntegerField(read_only=True)

    class Meta:
        model = Reply
        fields = ('comment', 'to_user_id', 'from_user', 'content', 'like_nums')


class ReplyDetailSerializer(serializers.ModelSerializer):

    from_user = UserDetailSerializer()
    to_user = serializers.SerializerMethodField()
    is_like = serializers.SerializerMethodField()

    def get_is_like(self, obj):
        user = self.context['request'].user
        if not isinstance(user, User):
            return False
        like = Like.objects.filter(user=user, like_id=obj.id, like_type='reply').first()
        if not like:
            return False
        return like.id

    def get_to_user(self, obj):
        user = User.objects.filter(id=obj.to_user_id)[0]
        to_user_serializer = UserDetailSerializer(user, context={'request': self.context['request']})
        return to_user_serializer.data

    def validate(self, attrs):
        del attrs['to_user_id']
        return attrs

    class Meta:
        model = Reply
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('article', 'content', 'user')


class CommentDetailSerializer(serializers.ModelSerializer):

    user = UserDetailSerializer()
    replys = ReplyDetailSerializer(many=True)

    is_like = serializers.SerializerMethodField()

    def get_is_like(self, obj):
        user = self.context['request'].user
        if not isinstance(user, User):
            return False
        like = Like.objects.filter(user=user, like_id=obj.id, like_type='comment').first()
        if not like:
            return False
        return like.id

    class Meta:
        model = Comment
        fields = '__all__'

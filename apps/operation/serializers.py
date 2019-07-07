"""
  Created by Amor on 2018-09-22
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Fav, Comment, Reply, Like, Message, Dynamics
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
        fields = ('comment', 'to_user', 'from_user', 'content', 'like_nums')


class ReplyDetailSerializer(serializers.ModelSerializer):

    to_user_id = serializers.IntegerField(write_only=True, label='接收者')
    from_user = UserDetailSerializer(read_only=True)
    to_user = UserDetailSerializer(read_only=True)
    is_like = serializers.SerializerMethodField(read_only=True)

    def validate_to_user_id(self, to_user_id):
        to_user = User.objects.filter(id=to_user_id).first()
        if not isinstance(to_user, User):
            raise serializers.ValidationError('没有找到该用户')
        return to_user_id

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
        attrs['to_user'] = User.objects.filter(id=attrs['to_user_id']).first()
        del attrs['to_user_id']
        return attrs

    class Meta:
        model = Reply
        exclude = ('status',)


class CommentSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('article', 'content', 'user')


class CommentDetailSerializer(serializers.ModelSerializer):

    user = UserDetailSerializer(read_only=True)
    is_like = serializers.SerializerMethodField(read_only=True)
    reply_nums = serializers.SerializerMethodField(read_only=True)

    def get_is_like(self, obj):
        user = self.context['request'].user
        if not isinstance(user, User):
            return False
        like = Like.objects.filter(user=user, like_id=obj.id, like_type='comment').first()
        if not like:
            return False
        return like.id

    def get_reply_nums(self, obj):
        reply_nums = obj.replys.count()
        return reply_nums

    class Meta:
        model = Comment
        exclude = ('status',)


class MessageSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        if obj.anonymous:
            user = User.objects.filter(id=999).first()
        else:
            user = obj.user
        user_serializer = UserDetailSerializer(user, context={'request': self.context['request']})
        return user_serializer.data

    class Meta:
        model = Message
        exclude = ('status', )


class DynamicsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dynamics
        exclude = ('status', )

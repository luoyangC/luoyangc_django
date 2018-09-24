"""
  Created by Amor on 2018-09-22
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Fav, Comment, Reply
from users.serializers import UserDetailSerializer

__author__ = '骆杨'


User = get_user_model()


class FavSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fav
        exclude = ('status', )


class ReplySerializer(serializers.ModelSerializer):

    to_user = serializers.HiddenField(default=1)
    from_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    like_nums = serializers.IntegerField(read_only=True)

    class Meta:
        model = Reply
        fields = ('comment', 'to_user', 'from_user', 'content', 'like_nums')


class ReplyDetailSerializer(serializers.ModelSerializer):

    from_user = UserDetailSerializer()
    user = User.objects.filter(id=1)[0]
    to_user = serializers.SerializerMethodField()

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

    class Meta:
        model = Comment
        fields = '__all__'

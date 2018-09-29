"""
  Created by Amor on 2018-09-22
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Category, Article
from apps.users.serializers import UserDetailSerializer
from operation.models import Like, Fav

__author__ = '骆杨'


User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title', 'info')


class ArticleSerializer(serializers.ModelSerializer):

    user = UserDetailSerializer()
    is_like = serializers.SerializerMethodField()
    is_fav = serializers.SerializerMethodField()

    def get_is_like(self, obj):
        user = self.context['request'].user
        if not isinstance(user, User):
            return False
        like = Like.objects.filter(user=user, like_id=obj.id, like_type='article').first()
        if not like:
            return False
        return like.id

    def get_is_fav(self, obj):
        user = self.context['request'].user
        if not isinstance(user, User):
            return False
        fav = Fav.objects.filter(user=user, article=obj).first()
        if not fav:
            return False
        return fav.id

    class Meta:
        model = Article
        exclude = ('status', )

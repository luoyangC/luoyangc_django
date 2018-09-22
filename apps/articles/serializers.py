"""
  Created by Amor on 2018-09-22
"""
from rest_framework import serializers

from .models import Category, Article

__author__ = '骆杨'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title', 'info')


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'

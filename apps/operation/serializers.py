"""
  Created by Amor on 2018-09-22
"""
from rest_framework import serializers

from .models import Fav, Comment, Reply

__author__ = '骆杨'


class FavSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fav
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Reply
        fields = '__all__'

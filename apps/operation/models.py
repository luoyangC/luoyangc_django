from django.db import models

from home.models import Base
from apps.users.models import UserProfile
from articles.models import Article
# Create your models here.


class Fav(Base):
    """
    用户收藏
    """
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='收藏的文章')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='收藏的用户')

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.article.title


class Comment(Base):
    """
    用户评论
    """
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='评论的文章')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='评论者')
    content = models.TextField(verbose_name='评论内容')
    like_nums = models.IntegerField(default=0, verbose_name='点赞数')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.article.title

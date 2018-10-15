from django.db import models
from mdeditor.fields import MDTextField

from home.models import Base
from apps.users.models import UserProfile
from articles.models import Article
# Create your models here.


class Fav(Base):
    """
    用户收藏
    """
    article = models.ForeignKey(Article, related_name='favs', on_delete=models.CASCADE, verbose_name='收藏的文章')
    user = models.ForeignKey(UserProfile, related_name='favs', on_delete=models.CASCADE, verbose_name='收藏的用户')

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.article.title


class Comment(Base):
    """
    用户评论
    """
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE, verbose_name='评论的文章')
    user = models.ForeignKey(UserProfile, related_name='comments', on_delete=models.CASCADE, verbose_name='评论者')
    image = models.ImageField(max_length=100, upload_to='image/comment/%Y/%m',
                              null=True, blank=True, verbose_name='评论图片')
    content = models.TextField(verbose_name='评论内容')
    like_nums = models.IntegerField(default=0, verbose_name='点赞数')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class Reply(Base):
    """
    用户回复
    """
    comment = models.ForeignKey(Comment, related_name='replys', on_delete=models.CASCADE, verbose_name='评论')
    to_user_id = models.IntegerField(null=False, blank=False, verbose_name='接收者')
    from_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='发送者')
    content = models.TextField(verbose_name='回复内容')
    like_nums = models.IntegerField(default=0, verbose_name='点赞数')
    image = models.ImageField(max_length=100, upload_to='image/reply/%Y/%m',
                              null=True, blank=True, verbose_name='回复图片')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class Like(Base):
    """
    用户点赞
    """
    LIKE_TYPE = (
        ('article', '文章'),
        ('comment', '评论'),
        ('reply', '回复')
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='用户')
    like_type = models.CharField(max_length=7, choices=LIKE_TYPE, verbose_name='点赞类型')
    like_id = models.IntegerField(verbose_name='被点赞的id')

    class Meta:
        verbose_name = '点赞'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.like_id)


class Message(Base):
    """
    留言
    """
    user = models.ForeignKey(UserProfile, default=999, on_delete=models.CASCADE, verbose_name='用户')
    content = models.TextField(verbose_name='留言信息')
    anonymous = models.BooleanField(default=True, verbose_name='是否匿名')

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class Dynamics(Base):
    """
    动态
    """
    content = MDTextField(null=True, blank=False, verbose_name='动态内容')

    class Meta:
        verbose_name = '动态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content

"""
  Created by Amor on 2018-09-29
"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Article
from operation.models import Like, Fav, Comment, Reply

__author__ = '骆杨'


@receiver(post_save, sender=Fav)
def add_fav(sender, instance=None, **kwargs):
    if instance:
        _article = Article.objects.get(id=instance.article.id)
        _article.fav_nums += 1
        _article.save()


@receiver(post_delete, sender=Fav)
def del_fav(sender, instance=None, **kwargs):
    if instance:
        _article = Article.objects.get(id=instance.article.id)
        if _article.fav_nums > 0:
            _article.fav_nums -= 1
        else:
            _article.fav_nums = 0
        _article.save()


@receiver(post_save, sender=Like)
def add_like(sender, instance=None, **kwargs):
    if instance and instance.like_type == 'article':
        _article = Article.objects.get(id=instance.like_id)
        _article.like_nums += 1
        _article.save()


@receiver(post_delete, sender=Like)
def del_like(sender, instance=None, **kwargs):
    if instance and instance.like_type == 'article':
        _article = Article.objects.get(id=instance.like_id)
        if _article.like_nums > 0:
            _article.like_nums -= 1
        else:
            _article.like_nums = 0
        _article.save()


@receiver(post_save, sender=Comment)
def add_comment(sender, instance=None, **kwargs):
    if instance:
        _article = Article.objects.get(id=instance.article.id)
        _article.comment_nums += 1
        _article.save()


@receiver(post_delete, sender=Comment)
def del_comment(sender, instance=None, **kwargs):
    if instance:
        _article = Article.objects.get(id=instance.article.id)
        if _article.comment_nums > 0:
            _article.comment_nums -= 1
        else:
            _article.comment_nums = 0
        _article.save()


@receiver(post_save, sender=Reply)
def add_reply(sender, instance=None, **kwargs):
    if instance:
        _article = Article.objects.get(id=instance.comment.article.id)
        _article.comment_nums += 1
        _article.save()


@receiver(post_delete, sender=Reply)
def del_reply(sender, instance=None, **kwargs):
    if instance:
        _article = Article.objects.get(id=instance.comment.article.id)
        if _article.comment_nums > 0:
            _article.comment_nums -= 1
        else:
            _article.comment_nums = 0
        _article.save()

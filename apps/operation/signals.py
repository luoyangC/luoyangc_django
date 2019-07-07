"""
  Created by Amor on 2018-09-29
"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Like, Comment, Reply

__author__ = '骆杨'


@receiver(post_save, sender=Like)
def add_like(sender, instance=None, **kwargs):
    if instance and instance.like_type == 'comment':
        _comment = Comment.objects.get(id=instance.like_id)
        _comment.like_nums += 1
        _comment.save()
    if instance and instance.like_type == 'reply':
        _reply = Reply.objects.get(id=instance.like_id)
        _reply.like_nums += 1
        _reply.save()


@receiver(post_delete, sender=Like)
def del_like(sender, instance=None, **kwargs):
    if instance and instance.like_type == 'comment':
        _comment = Comment.objects.get(id=instance.like_id)
        if _comment.like_nums > 0:
            _comment.like_nums -= 1
        else:
            _comment.like_nums = 0
        _comment.save()
    if instance and instance.like_type == 'reply':
        _reply = Reply.objects.get(id=instance.like_id)
        if _reply.like_nums > 0:
            _reply.like_nums -= 1
        else:
            _reply.like_nums = 0
        _reply.save()

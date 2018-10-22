"""
  Created by Amor on 2018-09-22
"""
import xadmin
from .models import Fav, Comment, Reply, Like, Message, Dynamics

__author__ = '骆杨'


class FavAdmin(object):
    model_icon = 'fa fa-star'


class CommentAdmin(object):
    model_icon = 'fa fa-commenting'


class ReplyAdmin(object):
    model_icon = 'fa fa-comments-o'


class LikeAdmin(object):
    model_icon = 'fa fa-thumbs-up'


class MessageAdmin(object):
    model_icon = 'fa fa-archive'


class DynamicsAdmin(object):
    model_icon = 'fa fa-at'


xadmin.site.register(Fav, FavAdmin)
xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(Reply, ReplyAdmin)
xadmin.site.register(Like, LikeAdmin)
xadmin.site.register(Message, MessageAdmin)
xadmin.site.register(Dynamics, DynamicsAdmin)

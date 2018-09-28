"""
  Created by Amor on 2018-09-22
"""
import xadmin
from .models import Fav, Comment, Reply, Like

__author__ = '骆杨'


class FavAdmin(object):
    model_icon = 'fa fa-star'


class CommentAdmin(object):
    model_icon = 'fa fa-commenting'


class ReplyAdmin(object):
    pass


class LikeAdmin(object):
    pass


xadmin.site.register(Fav, FavAdmin)
xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(Reply, ReplyAdmin)
xadmin.site.register(Like, LikeAdmin)

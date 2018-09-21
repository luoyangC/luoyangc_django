"""
  Created by Amor on 2018-09-22
"""
import xadmin
from .models import Fav, Comment

__author__ = '骆杨'


class FavAdmin(object):
    model_icon = 'fa fa-heart'


class CommentAdmin(object):
    model_icon = 'fa fa-commenting'


xadmin.site.register(Fav, FavAdmin)
xadmin.site.register(Comment, CommentAdmin)

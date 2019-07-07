"""
  Created by Amor on 2018-09-22
"""
import xadmin
from .models import Category, Article, Sentence

__author__ = '骆杨'


class CategoryAdmin(object):
    model_icon = 'fa fa-navicon'


class ArticleAdmin(object):
    model_icon = 'fa fa-bookmark'


class SentenceAdmin(object):
    pass


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Sentence, SentenceAdmin)

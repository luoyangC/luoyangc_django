"""
  Created by Amor on 2018-09-22
"""
import xadmin
from .models import Category, Article

__author__ = '骆杨'


class CategoryAdmin(object):
    model_icon = 'fa fa-navicon'


class ArticleAdmin(object):
    model_icon = 'fa fa-bookmark'


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Article, ArticleAdmin)

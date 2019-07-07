"""
  Created by Amor on 2018-09-21
"""
import xadmin
from django.contrib.auth import get_user_model

__author__ = '骆杨'


User = get_user_model()


class UserAdmin(object):
    model_icon = 'fa fa-user'


xadmin.site.unregister(User)
xadmin.site.register(User, UserAdmin)

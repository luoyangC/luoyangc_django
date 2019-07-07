"""
  Created by Amor on 2018-09-22
"""
import xadmin
from xadmin import views

__author__ = '骆杨'


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = 'luoyangc'
    site_footer = 'luoyangc在线'
    menu_style = 'accordion'


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)

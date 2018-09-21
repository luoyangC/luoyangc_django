"""
luoyangc URL Configuration
"""
import xadmin
from django.urls import path, include
from django.views.generic import RedirectView
from luoyangc.settings import MEDIA_ROOT
from django.views.static import serve

from home.views import Index

urlpatterns = [
    # 主页
    path('', Index.as_view(), name='index'),
    # 后台管理
    path('admin/', xadmin.site.urls),
    # 站点图标
    path('favicon.ico', RedirectView.as_view(url='static/favicon.ico')),
    # 媒体文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    # Markdown插件
    path('mdeditor/', include('mdeditor.urls')),
]

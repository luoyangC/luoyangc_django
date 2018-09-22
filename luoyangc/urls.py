"""
luoyangc URL Configuration
"""
import xadmin
from django.urls import path, include
from django.views.generic import RedirectView
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from luoyangc.settings import MEDIA_ROOT
from home.views import Index
from articles import views as article_views
from operation import views as operation_views


router = DefaultRouter()
# 文章分类
router.register('category', article_views.CategoryViewSet, base_name='category')
# 文章
router.register('article', article_views.ArticleViewSet, base_name='Article')
# 收藏
router.register('fav', operation_views.FavViewSet, base_name='fav')
# 评论
router.register('comment', operation_views.CommentViewSet, base_name='comment')
# 回复
router.register('reply', operation_views.ReplyViewSet, base_name='reply')


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
    # 文档功能
    path('docs/', include_docs_urls(title='文档')),
    # API入口
    path('api/', include(router.urls)),
]

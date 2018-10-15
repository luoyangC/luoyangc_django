"""
luoyangc URL Configuration
"""
import xadmin
from django.urls import path, include
from django.views.generic import RedirectView
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

from luoyangc.settings import MEDIA_ROOT
from home.views import IndexView, UploadView
from users import views as user_views
from articles import views as article_views
from operation import views as operation_views


router = DefaultRouter()

# 邮件
router.register('code', user_views.EmailCodeViewSet, base_name='code')
# 用户
router.register('user', user_views.UserViewSet, base_name='user')
# 分类
router.register('category', article_views.CategoryViewSet, base_name='category')
# 归档
router.register('archive', article_views.ArchiveViewSet, base_name='archive')
# 标签
router.register('tag', article_views.TagViewSet, base_name='tag')
# 简介
router.register('profile', article_views.ArticleProfileViewSet, base_name='profile')
# 文章
router.register('article', article_views.ArticleViewSet, base_name='Article')
# 收藏
router.register('fav', operation_views.FavViewSet, base_name='fav')
# 点赞
router.register('like', operation_views.LikeViewSet, base_name='like')
# 评论
router.register('comment', operation_views.CommentViewSet, base_name='comment')
# 回复
router.register('reply', operation_views.ReplyViewSet, base_name='reply')
# 留言
router.register('message', operation_views.MessageViewSet, base_name='message')
# 动态
router.register('dynamics', operation_views.DynamicsViewSet, base_name='dynamics')


urlpatterns = [
    # 主页
    path('', IndexView.as_view(), name='index'),
    # 后台管理
    path('admin/', xadmin.site.urls),
    # 站点图标
    path('favicon.ico', RedirectView.as_view(url='static/favicon.ico')),
    # 媒体文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    # Markdown插件
    path('mdeditor/', include('mdeditor.urls')),
    # DRF登录API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # 文档功能
    path('docs/', include_docs_urls(title='文档')),
    # 获取授权
    path('api/login/', obtain_jwt_token),
    # 上传文件
    path('api/upload/', UploadView.as_view(), name='upload'),
    # API入口
    path('api/', include(router.urls)),
]

from django.db import models
from django.contrib.auth.models import AbstractUser

from home.models import Base
from mdeditor.fields import MDTextField

# Create your models here.


class UserProfile(AbstractUser, Base):
    """
    用户信息
    """
    GENDER_TYPE = (
        ('male', '男'),
        ('female', '女'),
        ('unknown', '未知'),
    )

    nick_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='昵称')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生日期')
    gender = models.CharField(max_length=8, choices=GENDER_TYPE, default='unknown', verbose_name='性别')
    image = models.ImageField(max_length=100, upload_to='image/user/%Y/%m',
                              default='image/user/default/1.png', verbose_name='头像')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='电话')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='邮箱')
    github = models.URLField(max_length=100, null=True, blank=True, verbose_name='GitHub地址')
    gitee = models.URLField(max_length=100, null=True, blank=True, verbose_name='码云地址')
    profile = MDTextField(null=True, blank=True, verbose_name='个人简介')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(Base):
    """
    邮箱验证
    """
    SEND_TYPE = (
        ('register', '注册'),
        ('forget', '找回密码'),
        ('update', '修改邮箱')
    )
    code = models.CharField(max_length=100, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(max_length=10, choices=SEND_TYPE, verbose_name='验证码类型')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email

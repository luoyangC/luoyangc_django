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

    birthday = models.DateField(null=True, blank=True, verbose_name='出生日期')
    gender = models.CharField(max_length=8, choices=GENDER_TYPE, default='unknown', verbose_name='性别')
    image = models.ImageField(max_length=100, upload_to='image/user/%Y/%m',
                              default='image/user/default/1.png', verbose_name='头像')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='电话')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='邮箱')
    homepage = models.URLField(max_length=100, null=True, blank=True, verbose_name='个人主页')
    profile = MDTextField(null=True, blank=True, verbose_name='个人简介')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

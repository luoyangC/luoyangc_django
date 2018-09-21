# Generated by Django 2.0 on 2018-09-21 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, verbose_name='创建时间')),
                ('status', models.SmallIntegerField(default=1, verbose_name='状态')),
                ('title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('content', mdeditor.fields.MDTextField(null=True, verbose_name='文章内容')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/article/%Y/%m', verbose_name='封面图')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('view_nums', models.IntegerField(default=0, verbose_name='浏览数')),
                ('comment_nums', models.IntegerField(default=0, verbose_name='评论数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏数')),
                ('like_nums', models.IntegerField(default=0, verbose_name='点赞数')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_created=True, verbose_name='创建时间')),
                ('status', models.SmallIntegerField(default=1, verbose_name='状态')),
                ('title', models.CharField(max_length=100, verbose_name='分类标题')),
                ('info', models.CharField(blank=True, max_length=100, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Category', verbose_name='分类'),
        ),
    ]

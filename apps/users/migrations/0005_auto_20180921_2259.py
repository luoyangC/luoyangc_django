# Generated by Django 2.0 on 2018-09-21 14:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180921_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='create_time',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.SmallIntegerField(default=1, verbose_name='状态'),
        ),
    ]

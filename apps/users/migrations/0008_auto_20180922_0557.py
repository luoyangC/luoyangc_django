# Generated by Django 2.0 on 2018-09-21 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180922_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='create_time',
            field=models.DateTimeField(auto_created=True, verbose_name='创建时间'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-16 23:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0003_users_delete_customer"),
    ]

    operations = [
        migrations.AddField(
            model_name="users",
            name="avatar",
            field=models.ImageField(
                null=True, upload_to="img/%Y/%m/%d/", verbose_name="上传图片"
            ),
        ),
        migrations.AddField(
            model_name="users",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime.now, verbose_name="注册时间"
            ),
        ),
        migrations.AddField(
            model_name="users",
            name="email",
            field=models.EmailField(max_length=254, null=True, verbose_name="邮箱"),
        ),
        migrations.AddField(
            model_name="users",
            name="gender",
            field=models.CharField(default="secret", max_length=6, verbose_name="性别"),
        ),
        migrations.AddField(
            model_name="users",
            name="mobile",
            field=models.CharField(max_length=20, null=True, verbose_name="手机号"),
        ),
        migrations.AddField(
            model_name="users",
            name="name",
            field=models.CharField(blank=True, max_length=20, verbose_name="姓名"),
        ),
        migrations.AddField(
            model_name="users",
            name="nick_name",
            field=models.CharField(default="123", max_length=20, verbose_name="昵称"),
        ),
    ]

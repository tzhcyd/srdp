# Generated by Django 4.2.1 on 2023-10-11 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("task_id", models.IntegerField()),
                ("user_id", models.IntegerField()),
                ("Like", models.IntegerField()),
                ("body", models.TextField()),
                (
                    "picture",
                    models.ImageField(upload_to="img/%Y/%m/%d/", verbose_name="上传图片"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="评论发布时间"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Friend",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField()),
                ("friend_id", models.IntegerField()),
                ("created_at", models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name="Participation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField()),
                ("task_id", models.IntegerField()),
                (
                    "is_accepted",
                    models.BooleanField(default=False, verbose_name="是否接受邀请"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="参与任务时间"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tasks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("host_id", models.IntegerField()),
                ("parent_id", models.IntegerField()),
                (
                    "title",
                    models.CharField(default="任务", max_length=20, verbose_name="任务名称"),
                ),
                ("body", models.TextField()),
                ("text", models.TextField()),
                ("plan_start_time", models.DateTimeField(verbose_name="预计开始时间")),
                ("plan_end_time", models.TimeField(verbose_name="预计结束时间")),
                ("actual_start_time", models.TimeField(verbose_name="实际开始时间")),
                ("actual_end_time", models.TimeField(verbose_name="实际结束时间")),
                (
                    "is_completed",
                    models.BooleanField(default=False, verbose_name="是否完成任务"),
                ),
                ("loop_mode", models.BooleanField(default=False, verbose_name="是否重复")),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="任务创建时间"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField()),
                (
                    "name",
                    models.CharField(blank=True, max_length=20, verbose_name="姓名"),
                ),
                (
                    "email",
                    models.EmailField(max_length=254, null=True, verbose_name="邮箱"),
                ),
                (
                    "nick_name",
                    models.CharField(default="123", max_length=20, verbose_name="昵称"),
                ),
                (
                    "gender",
                    models.CharField(
                        default="secret", max_length=6, null=True, verbose_name="性别"
                    ),
                ),
                (
                    "mobile",
                    models.CharField(max_length=20, null=True, verbose_name="手机号"),
                ),
                (
                    "avatar",
                    models.ImageField(
                        null=True, upload_to="img/%Y/%m/%d/", verbose_name="上传图片"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="注册时间"
                    ),
                ),
            ],
        ),
    ]

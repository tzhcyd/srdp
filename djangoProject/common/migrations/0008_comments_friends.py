# Generated by Django 4.2.1 on 2023-05-17 00:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0007_tasks"),
    ]

    operations = [
        migrations.CreateModel(
            name="comments",
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
            name="friends",
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
                ("friends_id", models.IntegerField()),
                ("created_at", models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-17 00:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0006_alter_participation_task_id_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="tasks",
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
    ]

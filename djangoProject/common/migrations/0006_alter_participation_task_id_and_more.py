# Generated by Django 4.2.1 on 2023-05-17 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0005_participation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="participation",
            name="task_id",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="participation",
            name="user_id",
            field=models.IntegerField(),
        ),
    ]

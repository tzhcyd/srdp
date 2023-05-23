# Generated by Django 4.2.1 on 2023-05-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=200)),
                ("phonenumber", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name="comments",
        ),
        migrations.DeleteModel(
            name="friends",
        ),
        migrations.DeleteModel(
            name="participation",
        ),
        migrations.DeleteModel(
            name="tasks",
        ),
        migrations.DeleteModel(
            name="users",
        ),
    ]
# Generated by Django 4.2 on 2024-06-05 12:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Messages",
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
                ("qualtrics_id", models.CharField(max_length=255)),
                ("message", models.CharField(max_length=2550)),
                ("message_time", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Nicks",
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
                ("qualtrics_id", models.CharField(max_length=255)),
                ("nick", models.CharField(max_length=255)),
                ("chatroom_start", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
# Generated by Django 4.2 on 2024-06-27 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0004_angryreactions_heartreactions_likereactions_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="nicks",
            name="is_manipulation_positive",
            field=models.BooleanField(default=True),
        ),
    ]
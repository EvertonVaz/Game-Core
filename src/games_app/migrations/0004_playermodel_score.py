# Generated by Django 5.1.3 on 2024-11-24 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("games_app", "0003_alter_playermodel_gameid"),
    ]

    operations = [
        migrations.AddField(
            model_name="playermodel",
            name="score",
            field=models.IntegerField(default=0),
        ),
    ]

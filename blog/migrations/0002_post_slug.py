# Generated by Django 4.2.8 on 2023-12-06 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
    ]
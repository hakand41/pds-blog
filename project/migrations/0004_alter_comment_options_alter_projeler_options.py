# Generated by Django 4.1.3 on 2022-12-26 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0003_alter_comment_project"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["-created_at"]},
        ),
        migrations.AlterModelOptions(
            name="projeler",
            options={"ordering": ["-created_at"]},
        ),
    ]

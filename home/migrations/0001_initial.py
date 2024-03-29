# Generated by Django 4.1.3 on 2022-12-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Setting",
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
                ("title", models.CharField(max_length=50)),
                ("keywords", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=50)),
                ("company", models.CharField(max_length=50)),
                ("adress", models.CharField(blank=True, max_length=150)),
                ("fax", models.CharField(blank=True, max_length=50)),
                ("email", models.CharField(blank=True, max_length=50)),
                ("smtpserver", models.CharField(blank=True, max_length=50)),
                ("smtpemail", models.CharField(blank=True, max_length=50)),
                ("smtppassword", models.CharField(blank=True, max_length=50)),
                ("facebook", models.CharField(blank=True, max_length=50)),
                ("instagram", models.CharField(blank=True, max_length=50)),
                ("twitter", models.CharField(blank=True, max_length=50)),
                ("aboutus", models.CharField(blank=True, max_length=50)),
                ("contact", models.CharField(blank=True, max_length=50)),
                ("references", models.CharField(blank=True, max_length=50)),
                (
                    "status",
                    models.CharField(
                        choices=[("True", "Evet"), ("False", "Hayır")], max_length=10
                    ),
                ),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

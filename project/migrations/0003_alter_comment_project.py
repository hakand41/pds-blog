# Generated by Django 4.1.3 on 2022-12-26 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0002_remove_projeler_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="project.projeler",
            ),
        ),
    ]

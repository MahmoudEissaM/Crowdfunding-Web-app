# Generated by Django 5.2 on 2025-04-09 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_donation"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="related_projects",
            field=models.ManyToManyField(
                blank=True, related_name="linked_projects", to="projects.project"
            ),
        ),
    ]

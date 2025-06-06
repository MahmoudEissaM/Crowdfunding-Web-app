# Generated by Django 3.2.25 on 2025-04-09 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='home.Tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

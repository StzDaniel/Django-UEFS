# Generated by Django 5.0.6 on 2024-06-06 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_date',
        ),
    ]
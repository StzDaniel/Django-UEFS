# Generated by Django 5.0.6 on 2024-05-17 01:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('community_app', '0001_initial'),
        ('people_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('phone_number', models.IntegerField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('id_community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community_app.community')),
                ('id_people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people_app.people')),
            ],
        ),
    ]

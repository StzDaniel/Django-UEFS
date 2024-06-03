# Generated by Django 5.0.6 on 2024-05-26 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people_app', '0005_people_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=200),
        ),
        migrations.AlterField(
            model_name='people',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
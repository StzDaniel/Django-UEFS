#HEAD
# Generated by Django 5.0.6 on 2024-05-26 00:07
=======
# Generated by Django 5.0.6 on 2024-05-25 01:04
#4a6086e8ff925bdf7c26346a8d3c2588632141ea

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]

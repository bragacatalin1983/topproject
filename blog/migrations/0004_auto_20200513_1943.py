# Generated by Django 3.0.6 on 2020-05-13 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200507_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 13, 19, 43, 43, 820234)),
        ),
    ]

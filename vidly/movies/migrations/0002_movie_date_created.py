# Generated by Django 2.2 on 2022-05-17 10:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 10, 2, 7, 624648, tzinfo=utc)),
        ),
    ]

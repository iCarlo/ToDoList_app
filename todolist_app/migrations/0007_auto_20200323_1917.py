# Generated by Django 3.0.4 on 2020-03-23 11:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0006_auto_20200323_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 23, 11, 17, 40, 492226, tzinfo=utc)),
        ),
    ]

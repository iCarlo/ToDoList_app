# Generated by Django 3.0.4 on 2020-03-23 13:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0008_auto_20200323_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='added_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 3.0.4 on 2020-03-23 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0007_auto_20200323_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.CharField(default='', max_length=200),
        ),
    ]

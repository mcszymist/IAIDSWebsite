# Generated by Django 2.1.7 on 2019-03-30 18:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgAdminPanel', '0012_auto_20190328_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='endtime',
            field=models.TimeField(default=datetime.time(10, 6, 6, 135130)),
        ),
        migrations.AlterField(
            model_name='event',
            name='starttime',
            field=models.TimeField(default=datetime.time(10, 6, 6, 135084)),
        ),
        migrations.AlterField(
            model_name='job',
            name='endtime',
            field=models.TimeField(default=datetime.time(10, 6, 6, 141904)),
        ),
        migrations.AlterField(
            model_name='job',
            name='starttime',
            field=models.TimeField(default=datetime.time(10, 6, 6, 141867)),
        ),
    ]
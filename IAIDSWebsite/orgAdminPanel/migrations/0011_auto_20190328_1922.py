# Generated by Django 2.1.7 on 2019-03-29 03:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgAdminPanel', '0010_auto_20190326_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='endtime',
            field=models.TimeField(default=datetime.time(19, 22, 45, 335849)),
        ),
        migrations.AlterField(
            model_name='event',
            name='starttime',
            field=models.TimeField(default=datetime.time(19, 22, 45, 335795)),
        ),
        migrations.AlterField(
            model_name='job',
            name='endtime',
            field=models.TimeField(default=datetime.time(19, 22, 45, 344388)),
        ),
        migrations.AlterField(
            model_name='job',
            name='starttime',
            field=models.TimeField(default=datetime.time(19, 22, 45, 344344)),
        ),
    ]

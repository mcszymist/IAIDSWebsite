# Generated by Django 2.2 on 2019-04-14 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgAdminPanel', '0003_auto_20190402_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='endtime',
            field=models.TimeField(default=datetime.time(9, 5, 48, 495345)),
        ),
        migrations.AlterField(
            model_name='event',
            name='starttime',
            field=models.TimeField(default=datetime.time(9, 5, 48, 495318)),
        ),
        migrations.AlterField(
            model_name='job',
            name='endtime',
            field=models.TimeField(default=datetime.time(9, 5, 48, 498097)),
        ),
        migrations.AlterField(
            model_name='job',
            name='starttime',
            field=models.TimeField(default=datetime.time(9, 5, 48, 498079)),
        ),
    ]

# Generated by Django 2.1.2 on 2018-10-10 12:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ogbam', '0002_auto_20181010_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airtime',
            name='amount',
            field=models.CharField(blank=True, choices=[(100, '#100'), (500, '#500'), (1000, '#1000'), (5000, '#5000'), (1000, '#1000')], default='#100', max_length=30),
        ),
        migrations.AlterField(
            model_name='airtime',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 12, 22, 33, 148078, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='data',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 12, 22, 33, 153078, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='share_and_sell',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 12, 22, 33, 145078, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 10, 12, 22, 33, 151078, tzinfo=utc)),
        ),
    ]
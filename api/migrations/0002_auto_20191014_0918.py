# Generated by Django 2.2.6 on 2019-10-14 06:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.PositiveIntegerField(),
        ),
    ]

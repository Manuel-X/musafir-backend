# Generated by Django 2.2.6 on 2019-10-15 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20191015_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='date',
            new_name='date_of_booking',
        ),
    ]
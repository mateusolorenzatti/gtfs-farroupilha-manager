# Generated by Django 3.1.4 on 2020-12-23 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gtfs', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Agency',
        ),
        migrations.DeleteModel(
            name='Routes',
        ),
        migrations.DeleteModel(
            name='Shapes',
        ),
        migrations.DeleteModel(
            name='Stops',
        ),
        migrations.DeleteModel(
            name='StopTimes',
        ),
        migrations.DeleteModel(
            name='Trips',
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-23 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('route_id', models.IntegerField(primary_key=True, serialize=False)),
                ('route_short_name', models.CharField(blank=True, max_length=50, null=True)),
                ('route_long_name', models.CharField(blank=True, max_length=255, null=True)),
                ('route_desc', models.CharField(blank=True, max_length=255, null=True)),
                ('route_type', models.SmallIntegerField(blank=True, null=True)),
                ('route_url', models.CharField(blank=True, max_length=50, null=True)),
                ('route_color', models.CharField(blank=True, max_length=11, null=True)),
                ('route_text_color', models.CharField(blank=True, max_length=11, null=True)),
                ('route_sort_order', models.IntegerField(blank=True, null=True)),
                ('min_headway_minutes', models.IntegerField(blank=True, null=True)),
                ('eligibility_restricted', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'routes',
                'db_table': 'routes',
                'managed': False,
            },
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-23 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shapes',
            fields=[
                ('shape_id_serial', models.AutoField(primary_key=True, serialize=False)),
                ('shape_id', models.CharField(max_length=50)),
                ('shape_pt_lat', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('shape_pt_lon', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('shape_pt_sequence', models.IntegerField(blank=True, null=True)),
                ('shape_dist_traveled', models.DecimalField(blank=True, decimal_places=6, max_digits=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'shapes',
                'db_table': 'shapes',
                'managed': False,
            },
        ),
    ]
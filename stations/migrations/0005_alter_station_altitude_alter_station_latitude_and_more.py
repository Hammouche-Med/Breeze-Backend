# Generated by Django 4.0.6 on 2022-09-25 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0004_alter_station_metar_alter_station_synop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='altitude',
            field=models.FloatField(max_length=10),
        ),
        migrations.AlterField(
            model_name='station',
            name='latitude',
            field=models.FloatField(max_length=10),
        ),
        migrations.AlterField(
            model_name='station',
            name='longitude',
            field=models.FloatField(max_length=10),
        ),
    ]
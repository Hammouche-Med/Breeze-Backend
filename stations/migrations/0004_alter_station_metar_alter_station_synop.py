# Generated by Django 4.0.6 on 2022-09-05 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0003_remove_production_delay_3t'),
        ('stations', '0003_station_metar_station_synop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='metar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='metar', to='production.production'),
        ),
        migrations.AlterField(
            model_name='station',
            name='synop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='synop', to='production.production'),
        ),
    ]

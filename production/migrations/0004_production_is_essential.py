# Generated by Django 4.0.6 on 2022-09-17 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0003_remove_production_delay_3t'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='is_essential',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 4.0.6 on 2022-09-17 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0004_production_is_essential'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='full_day',
            field=models.BooleanField(default=False),
        ),
    ]

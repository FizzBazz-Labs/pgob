# Generated by Django 5.0.2 on 2024-04-16 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overflight_non_commercial_aircraft', '0009_alter_overflightnoncommercialaircraft_flight_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='overflightnoncommercialaircraft',
            name='reviewed_comment',
            field=models.TextField(blank=True),
        ),
    ]

# Generated by Django 5.0 on 2024-03-18 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overflight_non_commercial_aircraft', '0007_rename_jurisdiction_overflightnoncommercialaircraft_flight_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='overflightnoncommercialaircraft',
            name='fbo_attendant',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='overflightnoncommercialaircraft',
            name='flight_type',
            field=models.CharField(choices=[('CIVIL', 'Civil'), ('MILITARY', 'Militar'), ('EMERGENCY', 'Emergencia'), ('CHARTER', 'Charter'), ('OVERFLIGHT', 'Sobrevuelo'), ('TECHNICAL_SCALE', 'Escala Técnica')], default='CIVIL', max_length=50),
        ),
    ]

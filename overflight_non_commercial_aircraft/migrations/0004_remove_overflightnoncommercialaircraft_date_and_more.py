# Generated by Django 5.0 on 2024-03-05 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overflight_non_commercial_aircraft', '0003_remove_overflightnoncommercialaircraft_signature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='overflightnoncommercialaircraft',
            name='date',
        ),
        migrations.AlterField(
            model_name='overflightnoncommercialaircraft',
            name='jurisdiction',
            field=models.CharField(choices=[('CIVIL', 'Civil'), ('MILITARY', 'Militar')], default='CIVIL', max_length=50),
        ),
    ]
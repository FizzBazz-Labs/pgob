# Generated by Django 5.0 on 2024-02-29 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralVehicleAccreditation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission', models.CharField(max_length=150)),
                ('assigned_by', models.CharField(max_length=150)),
                ('distinctive', models.CharField(blank=True, max_length=150)),
                ('observations', models.CharField(blank=True, max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('vehicles', models.ManyToManyField(related_name='general_vehicle_accreditations', to='vehicles.vehicle')),
            ],
        ),
    ]

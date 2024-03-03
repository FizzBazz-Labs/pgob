# Generated by Django 5.0 on 2024-02-28 03:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityWeaponAccreditation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_date', models.DateField(verbose_name='Fecha de Control')),
                ('control_time', models.TimeField(verbose_name='Hora')),
                ('weapon', models.CharField(max_length=150, verbose_name='Arma')),
                ('brand', models.CharField(max_length=150, verbose_name='Marca')),
                ('model', models.CharField(max_length=150, verbose_name='Modelo')),
                ('type', models.CharField(max_length=150, verbose_name='Tipo')),
                ('serial', models.CharField(max_length=150, verbose_name='Serial No.')),
                ('caliber', models.CharField(max_length=150, verbose_name='Calibre')),
                ('chargers', models.IntegerField(verbose_name='Cantidad de Cargadores')),
                ('ammunition', models.IntegerField(verbose_name='Total de Municiones')),
                ('observations', models.TextField(blank=True, verbose_name='Observaciones: (detallar otros elementos de protección y detención)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('communication_items', models.ManyToManyField(blank=True, related_name='security_weapons', to='equipments.equipment', verbose_name='Elementos de Comunicación')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sw_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

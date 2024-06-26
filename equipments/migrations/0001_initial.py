# Generated by Django 5.0 on 2024-02-28 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=150, verbose_name='Marca')),
                ('model', models.CharField(blank=True, max_length=150, verbose_name='Modelo')),
                ('type', models.CharField(max_length=150, verbose_name='Tipo')),
                ('serial', models.CharField(blank=True, max_length=150, verbose_name='Serial No.')),
                ('frequency', models.CharField(blank=True, max_length=150, verbose_name='Frecuencia')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

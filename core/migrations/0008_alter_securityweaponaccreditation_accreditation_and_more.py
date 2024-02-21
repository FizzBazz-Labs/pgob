# Generated by Django 5.0 on 2024-02-21 17:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_securityweaponaccreditation_accreditation_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='securityweaponaccreditation',
            name='accreditation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sw_set', to='core.internationalaccreditation'),
        ),
        migrations.AlterField(
            model_name='securityweaponaccreditation',
            name='ammunition',
            field=models.IntegerField(verbose_name='Total de Municiones'),
        ),
        migrations.AlterField(
            model_name='securityweaponaccreditation',
            name='brand',
            field=models.CharField(max_length=150, verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='securityweaponaccreditation',
            name='caliber',
            field=models.CharField(max_length=150, verbose_name='Calibre'),
        ),
        migrations.AlterField(
            model_name='securityweaponaccreditation',
            name='chargers',
            field=models.IntegerField(verbose_name='Cantidad de Cargadores'),
        ),
        migrations.AlterField(
            model_name='securityweaponaccreditation',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sw_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='securityweaponaccreditation',
            name='equipment_frequency',
            field=models.CharField(max_length=150, verbose_name='Frecuencia'),
        ),
        migrations.AlterField(
            model_name='securityweaponaccreditation',
            name='equipment_model',
            field=models.CharField(max_length=150, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='securityweaponaccreditation',
            name='equipment_radio',
            field=models.CharField(max_length=150, verbose_name='Radio'),
        ),
        migrations.AlterField(
            model_name='securityweaponaccreditation',
            name='equipment_serial',
            field=models.CharField(max_length=150, verbose_name='Serie'),
        ),
        migrations.AlterField(
            model_name='securityweaponaccreditation',
            name='equipment_type',
            field=models.CharField(max_length=150, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='securityweaponaccreditation',
            name='model',
            field=models.CharField(max_length=150, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='securityweaponaccreditation',
            name='observations',
            field=models.TextField(blank=True, verbose_name='Observaciones: (detallar otros elementos de protección y detención)'),
        ),
        migrations.AlterField(
            model_name='securityweaponaccreditation',
            name='serial',
            field=models.CharField(max_length=150, verbose_name='Serial No.'),
        ),
        migrations.AlterField(
            model_name='securityweaponaccreditation',
            name='type',
            field=models.CharField(max_length=150, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='securityweaponaccreditation',
            name='weapon',
            field=models.CharField(max_length=150, verbose_name='Arma'),
        ),
    ]

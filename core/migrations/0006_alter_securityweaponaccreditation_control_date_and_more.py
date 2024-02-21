# Generated by Django 5.0.2 on 2024-02-21 06:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_internationalaccreditation_authorized_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='securityweaponaccreditation',
            name='control_date',
            field=models.DateField(verbose_name='Fecha de Control'),
        ),
        migrations.AlterField(
            model_name='securityweaponaccreditation',
            name='control_time',
            field=models.TimeField(verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='securityweaponaccreditation',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ws_forms', to=settings.AUTH_USER_MODEL),
        ),
    ]
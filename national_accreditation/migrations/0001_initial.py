# Generated by Django 5.0 on 2024-02-22 23:04

import django.db.models.deletion
import national_accreditation.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media_channels', '0001_initial'),
        ('positions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NationalAccreditation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=national_accreditation.models.image_filename)),
                ('first_name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=150, verbose_name='Apellido')),
                ('passport_id', models.CharField(max_length=100, verbose_name='Cédula /Pasaporte')),
                ('authorization_letter', models.FileField(blank=True, upload_to=national_accreditation.models.authorization_letter_filename)),
                ('institution', models.CharField(max_length=150, verbose_name='Institución')),
                ('address', models.CharField(max_length=150, verbose_name='Dirección')),
                ('phone_number', models.CharField(max_length=150, verbose_name='Teléfono')),
                ('phone_number_2', models.CharField(blank=True, max_length=150, verbose_name='Teléfono 2')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo Electrónico')),
                ('birthday', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('birthplace', models.CharField(max_length=250, verbose_name='Lugar de Nacimiento')),
                ('blood_type', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=150, verbose_name='Tipo de Sangre')),
                ('type', models.CharField(choices=[('coordinación_general', 'Coordinación General'), ('protocolo', 'Protocolo'), ('seguridad', 'Seguridad'), ('personal_técnico', 'Personal Técnico'), ('Delegación Oficial', 'Delegación Oficial'), ('enlace', 'Enlace'), ('proveedor', 'Proveedor'), ('comisión_de_prensa', 'Comisión de Prensa'), ('prensa_comercial', 'Prensa Comercial')], max_length=150, verbose_name='Tipo de Acreditación')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('authorized_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='national_forms_verifies', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='national_forms', to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('media_channel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='national_forms', to='media_channels.mediachannel')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='national_forms', to='positions.position', verbose_name='Cargo en el Evento')),
                ('sub_position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='national_forms', to='positions.subposition')),
            ],
        ),
    ]
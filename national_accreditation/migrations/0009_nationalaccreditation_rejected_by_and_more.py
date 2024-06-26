# Generated by Django 5.0.2 on 2024-03-12 21:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('national_accreditation', '0008_alter_nationalaccreditation_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='nationalaccreditation',
            name='rejected_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='national_rejected_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='nationalaccreditation',
            name='reviewed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='national_reviewed_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='nationalaccreditation',
            name='authorized_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='national_authorized_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='nationalaccreditation',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='national_forms', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='nationalaccreditation',
            name='type',
            field=models.CharField(blank=True, choices=[('GENERAL_COORDINATION', 'Coordinación General'), ('PROTOCOL', 'Protocolo'), ('SECURITY', 'Seguridad'), ('TECHNICAL_STAFF', 'Personal Técnico'), ('Delegación Oficial', 'Delegación Oficial'), ('LINK', 'Enlace'), ('SUPPLIER', 'Proveedor'), ('NEWSLETTER_COMMITTEE', 'Comisión de Prensa'), ('COMMERCIAL_NEWSLETTER', 'Prensa Comercial')], max_length=150, null=True),
        ),
    ]

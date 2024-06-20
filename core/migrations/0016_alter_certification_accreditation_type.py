# Generated by Django 5.0.6 on 2024-06-20 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_certification_accreditation_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='accreditation_type',
            field=models.CharField(choices=[('GENERAL_COORDINATION', 'Coordinación General'), ('PROTOCOL', 'Protocolo'), ('SECURITY', 'Seguridad'), ('TECHNICAL_STAFF', 'Personal Técnico'), ('OFFICIAL_DELEGATION', 'Delegación Oficial'), ('LINK', 'Enlace'), ('SUPPLIER', 'Proveedor'), ('NEWSLETTER_COMMITTEE', 'Comisión de Prensa'), ('COMMERCIAL_NEWSLETTER', 'Prensa Comercial'), ('OFFICIAL_DELEGATION_HEAD', 'Jefe de Delegación Oficial'), ('SUPPORT_STAFF', 'Personal de Apoyo'), ('OFFICIAL_NEWSLETTER', 'Prensa Oficial'), ('CREW', 'Tripulación'), ('INTERNATIONAL_NEWSLETTER', 'Prensa Internacional'), ('DIPLOMATIC_MISSION', 'Misión Diplomática'), ('MINREX_OFFICIALS', 'Funcionarios MINREX'), ('OFFICIAL_INTERNATIONAL_NEWSLETTER', 'Prensa Oficial Internacional')], default='GENERAL_COORDINATION', max_length=150),
        ),
    ]

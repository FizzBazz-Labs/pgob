# Generated by Django 5.0 on 2024-03-04 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('national_accreditation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nationalaccreditation',
            name='type',
            field=models.CharField(choices=[('GENERAL_COORDINATION', 'Coordinación General'), ('PROTOCOL', 'Protocolo'), ('SECURITY', 'Seguridad'), ('TECHNICAL_STAFF', 'Personal Técnico'), ('Delegación Oficial', 'Delegación Oficial'), ('LINK', 'Enlace'), ('SUPPLIER', 'Proveedor'), ('NEWSLETTER_COMMITTEE', 'Comisión de Prensa'), ('COMMERCIAL_NEWSLETTER', 'Prensa Comercial')], max_length=150, verbose_name='Tipo de Acreditación'),
        ),
    ]
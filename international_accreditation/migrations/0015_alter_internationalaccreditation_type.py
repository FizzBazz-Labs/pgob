# Generated by Django 5.0 on 2024-03-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('international_accreditation', '0014_internationalaccreditation_authorized_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internationalaccreditation',
            name='type',
            field=models.CharField(blank=True, choices=[('OFFICIAL_DELEGATION_HEAD', 'Jefe de Delegación Oficial'), ('OFFICIAL_DELEGATION', 'Delegación Oficial'), ('PROTOCOL', 'Protocolo'), ('SECURITY', 'Seguridad'), ('SUPPORT_STAFF', 'Personal de Apoyo'), ('OFFICIAL_NEWSLETTER', 'Prensa Oficial'), ('CREW', 'Tripulación'), ('COMMERCIAL_NEWSLETTER', 'Prensa Comercial')], max_length=150, null=True, verbose_name='Tipo de Acreditación'),
        ),
    ]

# Generated by Django 5.0.2 on 2024-05-07 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_siteconfiguration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accreditation_type', models.CharField(choices=[('GENERAL_COORDINATION', 'Coordinación General'), ('PROTOCOL', 'Protocolo'), ('SECURITY', 'Seguridad'), ('TECHNICAL_STAFF', 'Personal Técnico'), ('OFFICIAL_DELEGATION', 'Delegación Oficial'), ('LINK', 'Enlace'), ('SUPPLIER', 'Proveedor'), ('NEWSLETTER_COMMITTEE', 'Comisión de Prensa'), ('COMMERCIAL_NEWSLETTER', 'Prensa Comercial'), ('OFFICIAL_DELEGATION_HEAD', 'Jefe de Delegación Oficial'), ('SUPPORT_STAFF', 'Personal de Apoyo'), ('OFFICIAL_NEWSLETTER', 'Prensa Oficial'), ('CREW', 'Tripulación')], default='GENERAL_COORDINATION', max_length=150)),
                ('color', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

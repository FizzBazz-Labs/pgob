# Generated by Django 5.0.2 on 2024-05-07 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('national_accreditation', '0020_nationalaccreditation_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nationalaccreditation',
            old_name='downloaded',
            new_name='certificated',
        ),
        migrations.RenameField(
            model_name='nationalaccreditation',
            old_name='qr_code',
            new_name='certification',
        ),
    ]

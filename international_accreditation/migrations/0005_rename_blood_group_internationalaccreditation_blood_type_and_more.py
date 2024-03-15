# Generated by Django 5.0 on 2024-03-04 06:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('international_accreditation', '0004_alter_internationalaccreditation_allergies_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='internationalaccreditation',
            old_name='blood_group',
            new_name='blood_type',
        ),
        migrations.RemoveField(
            model_name='internationalaccreditation',
            name='age',
        ),
        migrations.RemoveField(
            model_name='internationalaccreditation',
            name='flight_arrival_date',
        ),
        migrations.RemoveField(
            model_name='internationalaccreditation',
            name='flight_arrival_time',
        ),
        migrations.RemoveField(
            model_name='internationalaccreditation',
            name='flight_departure_date',
        ),
        migrations.RemoveField(
            model_name='internationalaccreditation',
            name='flight_departure_time',
        ),
        migrations.AddField(
            model_name='internationalaccreditation',
            name='flight_arrival_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 4, 6, 20, 16, 590232, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='internationalaccreditation',
            name='flight_departure_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 4, 6, 20, 20, 770341, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='internationalaccreditation',
            name='type',
            field=models.CharField(choices=[('OFFICIAL_DELEGATION_HEAD', 'Official Delegation Head'), ('OFFICIAL_DELEGATION', 'Delegación Oficial'), ('PROTOCOL', 'Protocolo'), ('SECURITY', 'Seguridad'), ('SUPPORT_STAFF', 'Personal de Apoyo'), ('OFFICIAL_NEWSLETTER', 'Prensa Oficial'), ('CREW', 'Tripulación'), ('COMMERCIAL_NEWSLETTER', 'Prensa Comercial')], max_length=150, verbose_name='Tipo de Acreditación'),
        ),
    ]
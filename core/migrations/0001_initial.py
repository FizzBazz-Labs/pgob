# Generated by Django 5.0.2 on 2024-02-14 04:32

import core.models.international_accreditation
import core.models.national_accreditation
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CommunicationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('nationality', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='GeneralVehicleAccreditation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission', models.TextField()),
                ('vehicle_brand', models.CharField(max_length=150)),
                ('license_plate', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=150)),
                ('driver_name', models.CharField(max_length=150)),
                ('dip', models.CharField(max_length=150)),
                ('assigned', models.TextField()),
                ('distinctive', models.CharField(max_length=150)),
                ('observations', models.TextField()),
                ('responsible_signatures', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Inmunization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MediaChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=150)),
                ('color', models.CharField(max_length=150)),
                ('license_plate', models.CharField(max_length=20)),
                ('driver_name', models.CharField(max_length=150)),
                ('driver_id', models.CharField(max_length=20)),
                ('driver_phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WeaponType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CommunicationEquipmentDeclaration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_or_media', models.CharField(max_length=150)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.country')),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_type', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=150)),
                ('model', models.CharField(max_length=150)),
                ('serial_number', models.CharField(max_length=150)),
                ('approximate_value', models.IntegerField()),
                ('declaration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipments', to='core.communicationequipmentdeclaration')),
            ],
        ),
        migrations.CreateModel(
            name='OverflightNonCommercialAircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aircraft_type', models.CharField(max_length=150)),
                ('model', models.CharField(max_length=150)),
                ('civilian_military', models.CharField(choices=[('Civil', 'Civil'), ('Military', 'Military')], max_length=50)),
                ('registration_number', models.CharField(max_length=150)),
                ('color', models.CharField(max_length=150)),
                ('call_sign', models.CharField(max_length=150)),
                ('commander_name', models.CharField(max_length=150)),
                ('crew_members_count', models.IntegerField()),
                ('pmi_name', models.CharField(max_length=150)),
                ('passengers_count', models.IntegerField()),
                ('entry_date', models.DateField()),
                ('exit_date', models.DateField()),
                ('overflight_info', models.TextField()),
                ('landing_info', models.TextField()),
                ('origin', models.CharField(max_length=150)),
                ('destination', models.CharField(max_length=150)),
                ('route', models.CharField(max_length=150)),
                ('ground_facilities', models.TextField()),
                ('request_date', models.DateField()),
                ('requester_signature', models.CharField(max_length=150)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.country')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='flight_requests', to='core.position')),
            ],
        ),
        migrations.CreateModel(
            name='NationalAccreditation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to=core.models.national_accreditation.NationalAccreditation.create_image_path)),
                ('last_name', models.CharField(max_length=150)),
                ('passport_id', models.CharField(max_length=100)),
                ('letter_of_authorization', models.FileField(upload_to=core.models.national_accreditation.NationalAccreditation.upload_file_name)),
                ('institution', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=120)),
                ('cellphone', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('birthday', models.DateField()),
                ('birthplace', models.CharField(max_length=150)),
                ('blood_type', models.CharField(max_length=150)),
                ('accreditation_type', models.CharField(choices=[('Coordinacion General', 'Coordinacion General'), ('Protocolo', 'Protocolo'), ('Seguridad', 'Seguridad'), ('Personal tecnico', 'Personal tecnico'), ('Delegacion Oficial', 'Delegacion Oficial'), ('Enlace', 'Enlace'), ('Proveedor', 'Proveedor'), ('Comision de Prensa', 'Comision de Prensa'), ('Prensa Comercial', 'Prensa Comercial')], max_length=120)),
                ('authorized_by', models.CharField(max_length=150, null=True)),
                ('date', models.DateField()),
                ('media_channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='national_acreditation', to='core.mediachannel')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='national_acreditation', to='core.position')),
            ],
        ),
        migrations.CreateModel(
            name='InternationalAccreditation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to=core.models.international_accreditation.InternationalAccreditation.create_image_path)),
                ('last_name', models.CharField(max_length=150)),
                ('passport_id', models.CharField(max_length=100)),
                ('letter_of_authorization', models.FileField(upload_to=core.models.international_accreditation.InternationalAccreditation.create_image_path)),
                ('institution', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=120)),
                ('cellphone', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('birthday', models.DateField()),
                ('birthplace', models.CharField(max_length=150)),
                ('authorized_by', models.CharField(max_length=150, null=True)),
                ('date', models.DateField()),
                ('accreditation_type', models.CharField(choices=[('Jefe de delegacion oficial', 'jefe de delegacion oficial'), ('Delegacion Oficial', 'Delegacion Oficial'), ('Protocolo', 'Protocolo'), ('Seguridad', 'Seguridad'), ('Personal de apoyo', 'Personal de apoyo'), ('Prensa oficial', 'Prensa oficial'), ('Tripulacion', 'Tripulacion'), ('Prensa Comercial', 'Prensa Comercial')], max_length=120)),
                ('blood_type', models.CharField(max_length=150)),
                ('age', models.PositiveIntegerField(default=18)),
                ('diseases_under_treatment', models.CharField(max_length=150)),
                ('medications_in_use', models.CharField(max_length=200)),
                ('have_allergies', models.BooleanField(default=False)),
                ('has_inmunizations', models.BooleanField(default=False)),
                ('have_medical_history', models.BooleanField(default=False)),
                ('surgical_history', models.CharField(blank=True, max_length=150)),
                ('has_personal_doctor', models.BooleanField(default=False)),
                ('doctor_name', models.CharField(blank=True, max_length=100)),
                ('hotel_name', models.CharField(max_length=120)),
                ('hotel_address', models.CharField(max_length=120)),
                ('hotel_phone', models.CharField(max_length=120)),
                ('flight_arrival_date', models.DateField()),
                ('flight_arrival_time', models.TimeField()),
                ('flight_arrival_number', models.CharField(max_length=120)),
                ('fligth_procedence', models.CharField(max_length=120)),
                ('flight_departure_date', models.DateField()),
                ('flight_departure_time', models.TimeField()),
                ('flight_departure_number', models.CharField(max_length=120)),
                ('flight_destination', models.CharField(max_length=120)),
                ('allergies', models.ManyToManyField(blank=True, related_name='international_accreditations', to='core.allergy')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='international_accreditations', to='core.country')),
                ('inmunizations', models.ManyToManyField(blank=True, related_name='international_accreditations', to='core.inmunization')),
                ('media_channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='international_accreditations', to='core.mediachannel')),
                ('medical_histories', models.ManyToManyField(blank=True, related_name='international_accreditations', to='core.medicalhistory')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='international_accreditations', to='core.position')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleAccessAirport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsible_info', models.CharField(max_length=150)),
                ('responsible_signatures', models.TextField()),
                ('date', models.DateField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.country')),
                ('vehicles', models.ManyToManyField(related_name='accreditations', to='core.vehicle')),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.ManyToManyField(blank=True, related_name='vehicle', to='core.vehicletypes'),
        ),
        migrations.CreateModel(
            name='SecurityWeaponAccreditation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_control', models.DateField()),
                ('time_control', models.TimeField()),
                ('disclaimer_accepted', models.BooleanField(default=False)),
                ('weapon', models.CharField(max_length=150)),
                ('brand', models.CharField(max_length=150)),
                ('model', models.CharField(max_length=150)),
                ('serial_number', models.CharField(max_length=150)),
                ('caliber', models.CharField(max_length=150)),
                ('magazine_quantity', models.IntegerField()),
                ('ammunition_quantity', models.IntegerField()),
                ('communication_radio', models.CharField(max_length=150)),
                ('communication_model', models.CharField(max_length=150)),
                ('communication_serial', models.CharField(max_length=150)),
                ('communication_frequency', models.CharField(max_length=150)),
                ('communication_type', models.ManyToManyField(blank=True, related_name='security_accreditation', to='core.communicationtype')),
                ('weapon_type', models.ManyToManyField(blank=True, related_name='security_accreditation', to='core.weapontype')),
            ],
        ),
    ]

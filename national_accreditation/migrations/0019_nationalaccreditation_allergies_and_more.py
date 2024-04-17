# Generated by Django 5.0.2 on 2024-04-16 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allergies', '0001_initial'),
        ('immunizations', '0001_initial'),
        ('medical_histories', '0001_initial'),
        ('national_accreditation', '0018_alter_nationalaccreditation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='nationalaccreditation',
            name='allergies',
            field=models.ManyToManyField(blank=True, to='allergies.allergy'),
        ),
        migrations.AddField(
            model_name='nationalaccreditation',
            name='allergies_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='nationalaccreditation',
            name='diseases',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='nationalaccreditation',
            name='doctor_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='nationalaccreditation',
            name='immunizations',
            field=models.ManyToManyField(blank=True, to='immunizations.immunization'),
        ),
        migrations.AddField(
            model_name='nationalaccreditation',
            name='medicals',
            field=models.ManyToManyField(blank=True, to='medical_histories.medicalhistory'),
        ),
        migrations.AddField(
            model_name='nationalaccreditation',
            name='medication_1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='nationalaccreditation',
            name='medication_2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='nationalaccreditation',
            name='medication_3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='nationalaccreditation',
            name='medication_4',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='nationalaccreditation',
            name='surgical',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='nationalaccreditation',
            name='blood_type',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
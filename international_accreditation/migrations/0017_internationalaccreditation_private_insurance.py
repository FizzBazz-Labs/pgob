# Generated by Django 5.0 on 2024-03-14 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('international_accreditation', '0016_remove_internationalaccreditation_blood_rh_factor'),
    ]

    operations = [
        migrations.AddField(
            model_name='internationalaccreditation',
            name='private_insurance',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
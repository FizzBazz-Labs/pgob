# Generated by Django 5.0 on 2024-03-04 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('international_accreditation', '0005_rename_blood_group_internationalaccreditation_blood_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internationalaccreditation',
            name='phone_number_2',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]

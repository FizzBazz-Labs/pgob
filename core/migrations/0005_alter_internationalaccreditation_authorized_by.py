# Generated by Django 5.0.2 on 2024-02-21 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_internationalaccreditation_allergies_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internationalaccreditation',
            name='authorized_by',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]

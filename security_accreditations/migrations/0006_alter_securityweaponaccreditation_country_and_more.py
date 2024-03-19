# Generated by Django 5.0.3 on 2024-03-19 04:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("countries", "0001_initial"),
        ("positions", "0001_initial"),
        (
            "security_accreditations",
            "0005_securityweaponaccreditation_airportarrival_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="securityweaponaccreditation",
            name="country",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="security_weapons",
                to="countries.country",
            ),
        ),
        migrations.AlterField(
            model_name="securityweaponaccreditation",
            name="position",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="security_weapons",
                to="positions.position",
            ),
        ),
    ]
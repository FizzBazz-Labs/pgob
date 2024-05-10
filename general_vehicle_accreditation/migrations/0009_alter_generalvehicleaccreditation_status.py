# Generated by Django 5.0.6 on 2024-05-09 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "general_vehicle_accreditation",
            "0008_remove_generalvehicleaccreditation_mission_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="generalvehicleaccreditation",
            name="status",
            field=models.CharField(
                choices=[
                    ("PENDING", "Pendiente"),
                    ("REVIEWED", "Revisado"),
                    ("APPROVED", "Aprobado"),
                    ("REJECTED", "Rechazado"),
                ],
                default="PENDING",
                max_length=150,
            ),
        ),
    ]
# Generated by Django 5.0.1 on 2024-03-08 22:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "overflight_non_commercial_aircraft",
            "0004_remove_overflightnoncommercialaircraft_date_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="overflightnoncommercialaircraft",
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

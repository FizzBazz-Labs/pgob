# Generated by Django 5.0.1 on 2024-03-08 22:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "intercom_equipment_declaration",
            "0002_intercomequipmentdeclaration_created_by",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="intercomequipmentdeclaration",
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

# Generated by Django 5.0.6 on 2024-05-09 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("commerce", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commerce",
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

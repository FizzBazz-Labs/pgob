# Generated by Django 5.0.6 on 2024-05-15 04:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "intercom_equipment_declaration",
            "0007_alter_intercomequipmentdeclaration_status",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="intercomequipmentdeclaration",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="intercomequipmentdeclaration",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]

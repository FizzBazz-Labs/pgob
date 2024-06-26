# Generated by Django 5.0.6 on 2024-06-06 04:28

import intercom_equipment_declaration.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "intercom_equipment_declaration",
            "0008_intercomequipmentdeclaration_created_at_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="intercomequipmentdeclaration",
            name="authorized_comment",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="intercomequipmentdeclaration",
            name="certificated",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="intercomequipmentdeclaration",
            name="certification",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=intercom_equipment_declaration.models.get_declaration_country,
            ),
        ),
        migrations.AddField(
            model_name="intercomequipmentdeclaration",
            name="uuid",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="intercomequipmentdeclaration",
            name="reviewed_comment",
            field=models.TextField(blank=True, null=True),
        ),
    ]

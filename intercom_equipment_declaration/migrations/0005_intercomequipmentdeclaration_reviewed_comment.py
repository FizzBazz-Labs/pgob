# Generated by Django 5.0.2 on 2024-04-16 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intercom_equipment_declaration', '0004_intercomequipmentdeclaration_authorized_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='intercomequipmentdeclaration',
            name='reviewed_comment',
            field=models.TextField(blank=True),
        ),
    ]

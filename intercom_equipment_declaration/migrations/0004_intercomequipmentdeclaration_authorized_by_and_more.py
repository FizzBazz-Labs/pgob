# Generated by Django 5.0 on 2024-03-13 14:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intercom_equipment_declaration', '0003_intercomequipmentdeclaration_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='intercomequipmentdeclaration',
            name='authorized_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='communication_equipment_authorized_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='intercomequipmentdeclaration',
            name='rejected_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='communication_equipment_rejected_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='intercomequipmentdeclaration',
            name='reviewed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='communication_equipment_reviewed_set', to=settings.AUTH_USER_MODEL),
        ),
    ]

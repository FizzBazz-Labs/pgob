# Generated by Django 5.0 on 2024-02-29 01:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countries', '0001_initial'),
        ('equipments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntercomEquipmentDeclaration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=150)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intercom_equipment_declarations', to='countries.country')),
                ('equipments', models.ManyToManyField(blank=True, related_name='intercom_equipment_declarations', to='equipments.equipment')),
            ],
        ),
    ]
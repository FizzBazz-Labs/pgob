# Generated by Django 5.0.2 on 2024-04-17 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_alter_vehicle_circulation_card'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='circulation_card',
            new_name='tpv',
        ),
    ]
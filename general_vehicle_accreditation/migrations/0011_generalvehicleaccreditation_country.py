# Generated by Django 5.0.2 on 2024-05-10 04:49

import countries.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('countries', '0001_initial'),
        ('general_vehicle_accreditation', '0010_alter_generalvehicleaccreditation_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalvehicleaccreditation',
            name='country',
            field=models.ForeignKey(blank=True, default=countries.models.Country.get_default_pk,
                                    on_delete=django.db.models.deletion.PROTECT, to='countries.country'),
        ),
    ]

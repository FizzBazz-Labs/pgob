# Generated by Django 5.0.2 on 2024-04-16 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_vehicle_accreditation', '0006_generalvehicleaccreditation_reviewed_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalvehicleaccreditation',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('REVIEWED', 'Reviewed'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], default='PENDING', max_length=150),
        ),
    ]

# Generated by Django 5.0.2 on 2024-04-16 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('international_accreditation', '0023_internationalaccreditation_reviewed_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internationalaccreditation',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('REVIEWED', 'Reviewed'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], default='PENDING', max_length=150),
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-05 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('international_accreditation', '0009_alter_internationalaccreditation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internationalaccreditation',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pendiente'), ('REVIEWED', 'Revisado'), ('APPROVED', 'Aprobado'), ('REJECTED', 'Rechazado')], default='PENDING', max_length=150),
        ),
    ]
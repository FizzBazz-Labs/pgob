# Generated by Django 5.0.2 on 2024-03-12 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('national_accreditation', '0009_nationalaccreditation_rejected_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nationalaccreditation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

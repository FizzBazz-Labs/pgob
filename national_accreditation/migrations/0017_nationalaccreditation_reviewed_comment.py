# Generated by Django 5.0.2 on 2024-04-16 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('national_accreditation', '0016_nationalaccreditation_authorized_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='nationalaccreditation',
            name='reviewed_comment',
            field=models.TextField(blank=True),
        ),
    ]

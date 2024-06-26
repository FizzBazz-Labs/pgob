# Generated by Django 5.0.2 on 2024-05-24 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('national_accreditation', '0024_rename_times_updated_nationalaccreditation_times_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nationalaccreditation',
            name='allergies_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nationalaccreditation',
            name='authorized_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nationalaccreditation',
            name='reviewed_comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]

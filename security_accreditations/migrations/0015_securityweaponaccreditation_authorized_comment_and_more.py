# Generated by Django 5.0.6 on 2024-06-06 05:01

import security_accreditations.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("security_accreditations", "0014_alter_securityweaponaccreditation_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="securityweaponaccreditation",
            name="authorized_comment",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="securityweaponaccreditation",
            name="certificated",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="securityweaponaccreditation",
            name="certification",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=security_accreditations.models.get_declaration_country,
            ),
        ),
        migrations.AddField(
            model_name="securityweaponaccreditation",
            name="uuid",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="securityweaponaccreditation",
            name="reviewed_comment",
            field=models.TextField(blank=True, null=True),
        ),
    ]

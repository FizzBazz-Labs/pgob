# Generated by Django 5.0.6 on 2024-05-17 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "international_accreditation",
            "0028_alter_internationalaccreditation_flight_arrival_datetime_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="internationalaccreditation",
            name="times_edited",
            field=models.PositiveIntegerField(default=0),
        ),
    ]

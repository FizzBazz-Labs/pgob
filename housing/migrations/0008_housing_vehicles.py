# Generated by Django 5.0.2 on 2024-05-11 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0007_alter_housing_options_housing_authorized_comment_and_more'),
        ('vehicles', '0007_vehicle_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='housing',
            name='vehicles',
            field=models.ManyToManyField(blank=True, to='vehicles.vehicle'),
        ),
    ]

# Generated by Django 5.0.2 on 2024-05-23 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0010_housing_times_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housing',
            name='authorized_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housing',
            name='reviewed_comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]

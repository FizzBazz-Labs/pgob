# Generated by Django 5.0.2 on 2024-02-14 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subposition',
            name='position',
        ),
    ]

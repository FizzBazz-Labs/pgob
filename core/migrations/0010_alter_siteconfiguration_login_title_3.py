# Generated by Django 5.0.6 on 2024-05-25 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_siteconfiguration_login_title_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='login_title_3',
            field=models.CharField(blank=True, default='Acreditaciones', max_length=255, null=True),
        ),
    ]

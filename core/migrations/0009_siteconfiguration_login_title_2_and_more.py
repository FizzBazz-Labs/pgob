# Generated by Django 5.0.6 on 2024-05-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_alter_siteconfiguration_login_title_size"),
    ]

    operations = [
        migrations.AddField(
            model_name="siteconfiguration",
            name="login_title_2",
            field=models.CharField(default="Acreditaciones", max_length=255),
        ),
        migrations.AddField(
            model_name="siteconfiguration",
            name="login_title_3",
            field=models.CharField(default="Acreditaciones", max_length=255),
        ),
        migrations.AddField(
            model_name="siteconfiguration",
            name="use_bold",
            field=models.BooleanField(default=True),
        ),
    ]

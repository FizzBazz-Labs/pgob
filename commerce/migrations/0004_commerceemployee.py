# Generated by Django 5.0.2 on 2024-05-13 03:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0003_remove_commerce_authorized_comment_and_more'),
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommerceEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('passport_id', models.CharField(max_length=100)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('commerce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='commerce.commerce')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='countries.country')),
            ],
        ),
    ]

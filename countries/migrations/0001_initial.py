# Generated by Django 5.0.2 on 2024-02-14 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('nationality', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-27 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('rut', models.CharField(max_length=13)),
                ('cargo', models.CharField(max_length=25)),
                ('fono', models.CharField(max_length=9)),
                ('area', models.CharField(max_length=20)),
            ],
        ),
    ]
# Generated by Django 4.1.1 on 2022-12-06 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('primeraapp', '0002_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='primeraapp.area'),
        ),
    ]
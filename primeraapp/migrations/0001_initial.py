# Generated by Django 4.1.3 on 2022-12-05 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('marca', models.CharField(max_length=15)),
                ('fecha_expiracion', models.CharField(max_length=15)),
                ('peso', models.CharField(max_length=11)),
                ('area', models.CharField(max_length=15)),
            ],
        ),
    ]

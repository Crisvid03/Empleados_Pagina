# Generated by Django 5.0.4 on 2024-04-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_rename_deparmet_departamentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamentos',
            name='Funcionando',
            field=models.BooleanField(default=True, verbose_name='Funcionando'),
        ),
    ]
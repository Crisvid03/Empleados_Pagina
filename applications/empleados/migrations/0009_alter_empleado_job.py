# Generated by Django 5.0.4 on 2024-04-10 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0008_empleado_hojavia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='job',
            field=models.CharField(choices=[('0', 'Contador '), ('1', 'Gerente '), ('2', 'Economista '), ('3', 'Programador'), ('4', 'Otro'), ('5', 'Administrados'), ('6', 'Psicologo'), ('7', 'Ingeniro ambiental')], max_length=1, verbose_name='Labor '),
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-29 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0012_empleado_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='job',
            field=models.CharField(choices=[('0', 'CONTADOR'), ('1', 'GERENTE'), ('2', 'ECONOMISTA'), ('3', 'PROGRAMADOR'), ('4', 'OTRO'), ('5', 'ADMINISTRADOR'), ('6', 'PSICOLOGO'), ('7', 'INGENIER AMBIENTAL')], max_length=1, verbose_name='Labor '),
        ),
    ]

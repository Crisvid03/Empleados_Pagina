# Generated by Django 5.0.4 on 2024-04-21 22:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0009_alter_empleado_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='hojaVia',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
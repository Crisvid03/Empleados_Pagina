# Generated by Django 5.0.4 on 2024-04-10 16:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0007_alter_empleado_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='hojaVia',
            field=ckeditor.fields.RichTextField(default='texto'),
            preserve_default=False,
        ),
    ]
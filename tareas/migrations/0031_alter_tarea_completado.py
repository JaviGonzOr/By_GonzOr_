# Generated by Django 4.1.3 on 2023-03-21 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0030_alter_tarea_modelo_alter_tarea_proveedor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='completado',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

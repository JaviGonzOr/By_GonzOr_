# Generated by Django 4.1.3 on 2023-02-07 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0015_remove_tarea_imagen_tarea_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='imagen',
        ),
    ]

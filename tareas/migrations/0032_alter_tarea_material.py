# Generated by Django 4.1.3 on 2023-03-21 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0031_alter_tarea_completado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='material',
            field=models.TextField(blank=True, null=True),
        ),
    ]
# Generated by Django 4.1.3 on 2023-03-24 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0037_alter_visitas_creacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitas',
            old_name='creacion',
            new_name='visita',
        ),
    ]
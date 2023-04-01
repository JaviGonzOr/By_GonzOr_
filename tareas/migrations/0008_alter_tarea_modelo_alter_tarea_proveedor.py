# Generated by Django 4.1.3 on 2022-12-31 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0007_alter_tarea_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='modelo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tareas.producto'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tareas.proveedor'),
        ),
    ]

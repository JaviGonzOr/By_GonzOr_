# Generated by Django 4.1.3 on 2023-03-21 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0028_delete_montajes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('cliente', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('observaciones', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='tarea',
            name='completado',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tareas.proveedor'),
        ),
    ]

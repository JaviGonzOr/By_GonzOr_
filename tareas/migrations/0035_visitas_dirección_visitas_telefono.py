# Generated by Django 4.1.3 on 2023-03-23 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0034_visitas_creacion_visitas_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitas',
            name='dirección',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visitas',
            name='telefono',
            field=models.CharField(default=2, max_length=25),
            preserve_default=False,
        ),
    ]

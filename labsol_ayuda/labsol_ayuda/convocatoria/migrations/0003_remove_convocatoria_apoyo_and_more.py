# Generated by Django 4.0.2 on 2022-09-22 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocatoria', '0002_convocatoria_fecha_cierre_convocatoria_fecha_inicio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convocatoria',
            name='apoyo',
        ),
        migrations.RemoveField(
            model_name='convocatoria',
            name='decripcion',
        ),
        migrations.RemoveField(
            model_name='convocatoria',
            name='presupuesto',
        ),
        migrations.AlterField(
            model_name='convocatoria',
            name='fecha_cierre',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='convocatoria',
            name='fecha_inicio',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='convocatoria',
            name='hora_cierre',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='convocatoria',
            name='hora_inicio',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='convocatoria',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

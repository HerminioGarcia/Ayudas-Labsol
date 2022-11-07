# Generated by Django 4.0.2 on 2022-11-03 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Formulario', '0005_alter_campo_campo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campo',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='campo',
            name='formularios',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campos', to='Formulario.formularios', verbose_name='Modalidad'),
        ),
    ]

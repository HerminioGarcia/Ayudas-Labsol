# Generated by Django 4.0.2 on 2022-10-14 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Formulario', '0003_remove_formularios_subcategoria_delete_subcategoria'),
        ('convocatoria', '0003_remove_convocatoria_apoyo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='convocatoria',
            name='formularios',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='Formulario.formularios', verbose_name='Formularios'),
        ),
    ]

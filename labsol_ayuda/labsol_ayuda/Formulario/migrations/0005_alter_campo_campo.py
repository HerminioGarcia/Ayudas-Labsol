# Generated by Django 4.0.2 on 2022-11-01 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formulario', '0004_alter_campo_campo_alter_campo_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campo',
            name='campo',
            field=models.CharField(max_length=150),
        ),
    ]

# Generated by Django 4.0.2 on 2022-09-21 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulaio0',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_campos', models.CharField(max_length=4)),
                ('nombre_formulario', models.CharField(max_length=150, unique=True, verbose_name='Nombre del formulario')),
            ],
        ),
        migrations.CreateModel(
            name='Formulario_dinamico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formulario0', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fdinamico', to='Formulario.formulaio0', verbose_name='Formulario0')),
            ],
        ),
    ]

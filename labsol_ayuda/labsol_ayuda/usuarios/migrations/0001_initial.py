# Generated by Django 4.0.2 on 2022-07-14 18:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electronico')),
                ('first_name', models.CharField(max_length=150, verbose_name='Nombre(s)')),
                ('last_name', models.CharField(max_length=150, verbose_name='Apellido(s)')),
                ('curp', models.CharField(max_length=18, unique=True, validators=[django.core.validators.RegexValidator(code='curp_invalido', message='El CURP no tiene un formato válido', regex='^([A-Z][AEIOUX][A-Z]{2}\\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\\d])(\\d)$')], verbose_name='C.U.R.P.')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.estado', verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='DatosPersonales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(choices=[('1', 'Masculino'), ('2', 'Femenino'), ('3', 'Otro')], default=1, max_length=1, verbose_name='Género')),
                ('telefono', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='telCelular_invalido', message='Numero de telefono invalido', regex='^(\\d{10})$')], verbose_name='Teléfono Celular')),
                ('telefonoP', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(code='telCelular_invalido', message='Numero de telefono invalido', regex='^(\\d{10})$')], verbose_name='Teléfono Particular')),
                ('calle', models.CharField(max_length=150, verbose_name='Calle')),
                ('colonia', models.CharField(max_length=150, verbose_name='Colonia')),
                ('nexterno', models.CharField(max_length=10, verbose_name='Numero Externo')),
                ('ninterno', models.CharField(blank=True, max_length=10, null=True, verbose_name='Numero Interno')),
                ('cpostal', models.CharField(max_length=5, unique=True, validators=[django.core.validators.RegexValidator(code='codigoPostal_invalido', message='El Codigo postal no tiene un formato válido', regex='^(\\d{5})$')], verbose_name='Codigo Postal')),
                ('grado_estudio', models.CharField(choices=[('1', 'Licenciatura'), ('2', 'Maestría'), ('3', 'Doctorado'), ('4', 'Posdoctorado')], default=1, max_length=1, verbose_name='Último grado de estudios')),
                ('instituto', models.CharField(max_length=150, verbose_name='Institución a la que pertenece')),
                ('apoyo', models.CharField(choices=[('1', 'Apoyo personal'), ('2', 'Apoyo institucional')], default=1, max_length=1, verbose_name='Tipo de apoyo')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.estado', verbose_name='Estado')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.municipio', verbose_name='Municipio')),
                ('userD', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='datos', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]

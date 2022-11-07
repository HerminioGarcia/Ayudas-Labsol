from django.db import models
from usuarios.validadores import  curp_validador,codigoPos_validador,telefono_validador
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth import get_user_model

GENERO = [
    ('1', 'Masculino'),
    ('2', 'Femenino'),
    ('3', 'Otro'),
]

GRADO_STUDIO=[
    ('1', 'Licenciatura'),
    ('2', 'Maestría'),
    ('3', 'Doctorado'),
    ('4', 'Posdoctorado'),
    ]

TIPO_APOYO=[
    ('1', 'Apoyo personal'),
    ('2', 'Apoyo institucional'),
    ]

class Estado(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.ForeignKey("usuarios.Estado", verbose_name="Estado", on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.nombre



class AdministradorCuentasPersonalizadas(BaseUserManager):

    def create_superuser(self,email, curp, first_name, last_name, password, **other_fields):
        
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe estar asignado a is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe estar asignado a is_superuser=True')

        return self.create_user(email, curp, first_name, last_name, password, **other_fields)

    def create_user(self, email, curp, first_name, last_name, password, **other_fields):
        
        if not email:
            raise ValueError('Debe proporcionar una dirección de correo electrónico')
        
        email = self.normalize_email(email)
        user = self.model(email=email, curp=curp, first_name=first_name, last_name=last_name,**other_fields)
        user.set_password(password)
        user.save()
        
        return user

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField('Correo Electronico',unique=True)
    first_name= models.CharField("Nombre(s)",max_length=150)
    last_name = models.CharField("Apellido(s)",max_length=150)
    curp = models.CharField("C.U.R.P.", max_length=18, validators=[curp_validador],unique=True)
    is_staff= models.BooleanField(default=False)
    is_active= models.BooleanField(default=False)
    date_joined=models.DateTimeField(default=timezone.now)
    objects = AdministradorCuentasPersonalizadas()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['curp','first_name','last_name']
    def __str__(self):
        return self.email

class DatosPersonales(models.Model):
    user = models.OneToOneField(get_user_model(), verbose_name="Usuario", related_name='datos', on_delete=models.CASCADE)
    genero = models.CharField('Género', max_length=1, choices=GENERO,default=1,null=False)
    telefono = models.CharField("Teléfono Celular", max_length=10, validators=[telefono_validador],unique=True,null=False)
    telefonoP = models.CharField("Teléfono Particular*", max_length=10, validators=[telefono_validador],null=True, blank=True)
    estado = models.ForeignKey("usuarios.Estado", verbose_name="Estado",default=32, on_delete=models.DO_NOTHING,null=False)
    municipio = models.ForeignKey("usuarios.Municipio", verbose_name="Municipio", on_delete=models.DO_NOTHING,null=False)
    cpostal = models.CharField("Codigo Postal", max_length=5, validators=[codigoPos_validador],unique=False,null=False)
    calle = models.CharField("Calle", max_length=150,null=False)
    colonia = models.CharField("Colonia", max_length=150,null=False)
    nexterno = models.CharField("Numero Externo", max_length=10,null=False)
    ninterno = models.CharField("Numero Interno*", max_length=10,null=True, blank=True)
    grado_estudio = models.CharField('Último grado de estudios', max_length=1, choices=GRADO_STUDIO,default=1,null=False)
    instituto = models.CharField("Institución a la que pertenece",max_length=150,null=False)
    apoyo = models.CharField('Tipo de apoyo', max_length=1, choices=TIPO_APOYO,default=1,null=False)
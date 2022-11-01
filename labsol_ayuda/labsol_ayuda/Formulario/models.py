from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
#,unique=True
class Formularios(models.Model):
    nombre = models.CharField(max_length=50,unique=True)
    descripcion = models.TextField("Descripción", max_length=250)
    
    def __str__(self):
        return self.nombre
    
SI_NO=[
    ('1','Si'),
    ('0','No'),
]
SIZE_TEXTO = [
    (25,'25'),
    (50,'50'),
    (100,'100'),
    (150,'150'),
    (200,'200'),
    (300,'300'),
    (500,'500'),

]
TIPO_DATO=[
    ('1','Texto'),
    ('2','Númerico'),
    ('3','Decimal'),
    ('4','Fecha'),
    ('5','Fecha y hora'),
    ('6','Correo electrónico'),
    ('7','Selección (Combo)'),
    ('8','Selección (Opciones)'),
    ('9','Archivo PDF'),
]

class Campo(models.Model):
    campo = models.CharField(max_length=150)
    descripcion = models.TextField("Descripción", max_length=250)
    requerida = models.CharField(choices=SI_NO, max_length=1)
    tipo_dato = models.CharField("Tipo de respuesta", max_length=2, choices=TIPO_DATO)
    size_texto = models.SmallIntegerField("Máximo de palabras apróximadamente", null=True, 
    blank=True, choices=SIZE_TEXTO)
    formularios = models.ForeignKey("Formulario.Formularios", verbose_name="Campo", 
    on_delete=models.CASCADE, related_name='campos')
    
    def __str__(self):
        return self.campo
    
class OpcionesCampo(models.Model):
    opcion = models.CharField("Opción", max_length=150)
    valor = models.CharField(max_length=2)
    campo = models.ForeignKey("Formulario.Campo", verbose_name="Opciones", 
    on_delete=models.CASCADE, related_name='opciones_campo')
    
    def __str__(self):
        return self.opcion
    
class ContestaFormularios(models.Model):
    fecha = models.DateTimeField("Fecha", auto_now=True)
    formularios = models.ForeignKey("Formulario.Formularios", verbose_name="Formularios", on_delete=models.CASCADE)
    User = get_user_model()
    usuario = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.formularios.nombre + self.usuario.email
    
class DetalleContestaFormularios(models.Model):
    campo = models.ForeignKey("Formulario.Campo", verbose_name="Campo", on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=1500)
       
    contesta_formularios = models.ForeignKey("Formulario.ContestaFormularios", verbose_name="Contesta", on_delete=models.CASCADE)
     
    
    def __str__(self):
        return self.campo.campo + self.respuesta
from django.db import models
from Formulario.models import Formularios

APOYO = [
    ('1', 'Apoyo1'),
    ('2', 'Apoyo2'),
    ('3', 'Apoyo3'),
]

class Convocatoria(models.Model):
    nombre = models.CharField(max_length=100,unique=True)  
    fecha_inicio = models.DateField(null=False)
    hora_inicio = models.TimeField(null=False)
    fecha_cierre = models.DateField(null=False)
    hora_cierre = models.TimeField(null=False)
    formularios = models.OneToOneField(Formularios, verbose_name="Formularios",default=1, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
class Presupuesto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField('Descripción', null=True, blank=True)
    def __str__(self):
        return self.nombre

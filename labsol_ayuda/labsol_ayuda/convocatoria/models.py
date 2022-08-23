from django.db import models

APOYO = [
    ('1', 'Apoyo1'),
    ('2', 'Apoyo2'),
    ('3', 'Apoyo3'),
]

class Convocatoria(models.Model):
    nombre = models.CharField(max_length=100)
    decripcion = models.TextField('Descripción', null=True, blank=True)
    apoyo = models.CharField('Apoyo', max_length=1, choices=APOYO)
    presupuesto = models.ForeignKey("convocatoria.Presupuesto", verbose_name="Presupuesto", on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.nombre
    
class Presupuesto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField('Descripción', null=True, blank=True)
    def __str__(self):
        return self.nombre

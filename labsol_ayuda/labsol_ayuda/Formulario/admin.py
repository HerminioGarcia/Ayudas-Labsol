from django.contrib import admin
from . import models

admin.site.register(models.Categoria)
admin.site.register(models.Formularios)
admin.site.register(models.Campo)
admin.site.register(models.ContestaFormularios)
admin.site.register(models.DetalleContestaFormularios)
admin.site.register(models.OpcionesCampo)
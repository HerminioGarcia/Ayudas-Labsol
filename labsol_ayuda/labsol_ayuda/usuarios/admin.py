from django.contrib import admin
from usuarios.models import DatosPersonales,Estado, Municipio,User

admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(DatosPersonales)

admin.site.register(User)

from django.contrib import admin
from django.urls import path, include
from usuarios import views
#agregamos settings y static para lo la subida de archivos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('datosPersonales/', include('usuarios.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('', include('convocatoria.urls')),
    path('modalidades/', include('Formulario.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#agregamos esta linea para dirigirnos los documentos a media
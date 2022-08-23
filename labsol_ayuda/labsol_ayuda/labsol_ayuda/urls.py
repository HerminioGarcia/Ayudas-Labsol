from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from usuarios import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('datosPersonales/', include('usuarios.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('', include('convocatoria.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

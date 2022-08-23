from django.urls import path, include
from usuarios import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Bienbenida del sitio
    path('', login_required(views.BienvenidaView.as_view()), name='bienvenida'),

    path('usuarios_lista', login_required(views.ListaUsuariosView.as_view()), name='usuarios_lista'),

    path('grupos', views.AsignarGruposUsuario, name='asignar_grupos_usuario'),
    
    path('salir', login_required(LogoutView.as_view()), name='logout'),

    path('eliminar/<int:id>', views.eliminar_usuarios, name='eliminar_usuarios'),
    
    path('entrar', views.LoginView.as_view(), name='login'),

    path('registrar', views.RegistrarView.as_view(), name='registrar'),

    path('perfil', login_required(views.CrearPerfilView.as_view()), name='perfil'),
    
    path('activar/<slug:uidb64>/<slug:token>', views.ActivarCuentaView.as_view(), name='activar'),

    path('municipios', views.busca_municipios, name='busca_municipios'),

]

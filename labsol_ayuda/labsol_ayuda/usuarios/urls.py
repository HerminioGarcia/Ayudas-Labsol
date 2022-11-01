from django.urls import path, re_path, include
from usuarios import views
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Bienbenida del sitio
    path('', login_required(views.BienvenidaView.as_view()), name='bienvenida'),

    path('usuarios_lista', login_required(views.ListaUsuariosView.as_view()), name='usuarios_lista'),

    path('grupos', views.AsignarGruposUsuario, name='asignar_grupos_usuario'),
    
    path('salir', login_required(LogoutView.as_view()), name='logout'),

    # path('eliminar_usuario/<int:pk>', views.EliminarUsuarioView.as_view(), name='eliminar_usuario'),

    path('eliminar/<int:id>', views.eliminar_usuario, name='eliminar_usuario2'),
    
    path('entrar', views.LoginView.as_view(), name='login'),

    path('registrar', views.RegistrarView.as_view(), name='registrar'),

    path('perfil', login_required(views.CrearPerfilView.as_view()), name='perfil'),

    path('perfilEditar', views.EditarPerfilView.as_view(), name='perfilEditar'),
    
    path('activar/<slug:uidb64>/<slug:token>', views.ActivarCuentaView.as_view(), name='activar'),

    path('municipios', views.busca_municipios, name='busca_municipios'),

    path('reset/password_reset', PasswordResetView.as_view(template_name='registration/password_reset_form.html'
    , email_template_name="registration/password_reset_email.html"), name = 'password_reset'),
    
    path('reset/password_reset_done', 
    PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), 
    name = 'password_reset_done'),
    
    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', 
    PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), 
    name = 'password_reset_confirm'),
    
    path('reset/done',
    PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), 
    name = 'password_reset_complete'),
]

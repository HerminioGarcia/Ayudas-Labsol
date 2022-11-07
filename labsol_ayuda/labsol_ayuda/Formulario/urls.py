from django.urls import path
from Formulario import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('ModalidadesLista', login_required(views.ListaFormulario.as_view()), name='modalidades_lista'),

    path('Nueva', login_required(views.CrearFormularioView.as_view()), name='nuevoFormulario'),

    path('Editar/<int:pk>', login_required(views.EditarFormularioView.as_view()), name='editarFormulario'),

    path('eliminar/<int:id>', views.eliminar_formulario, name='eliminar_Formulario'),

    path('responder/<int:id>', views.formulario, name='formulario'),
    
    path('campo/Nuevo', login_required(views.NuevoCampoView.as_view()), name='nueva_campo2'),

    path('campos/<int:pk>', login_required(views.ModalidadesCamposLista.as_view()), name='campos_Lista'),

    path('eliminar/campo/<int:id>', views.eliminar_campo, name='eliminar_campo'),
    
    #esto es de prueba

    path('editar/campo/<int:id>', views.editar_campo, name='editar_campo'),
]

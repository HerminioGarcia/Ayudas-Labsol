from django.urls import path
from Formulario import views


urlpatterns = [
    path('ModalidadesLista', views.ListaFormulario.as_view(), name='modalidades_lista'),

    path('formularioNuevo', views.CrearFormularioView.as_view(), name='nuevoFormulario'),

    path('formularioEditar/<int:pk>', views.EditarFormularioView.as_view(), name='editarFormulario'),

    path('eliminar/<int:id>', views.eliminar_formulario, name='eliminar_Formulario'),

    path('formulario/<int:id>', views.formulario, name='formulario'),
    
    path('campoNuevo', views.NuevoCampoView.as_view(), name='nueva_campo'),

    path('campos/<int:pk>', views.ModalidadesCamposLista.as_view(), name='campos_Lista'),

    path('eliminar_Campo/<int:id>', views.eliminar_campo, name='eliminar_campo'),

    path('campoEditar/<int:pk>', views.EditarCampoView.as_view(), name='editarCampo'),
    
    #esto es de prueba

    path('editar/campo/<int:id>', views.editar_campo, name='editar_campo'),

    path('campo/nuevo', views.nuevo_campo, name='nuevo_campo'),

]

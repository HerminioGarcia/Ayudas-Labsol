from django.urls import path
from convocatoria import views, views_presupuesto
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('convocatoria/', login_required(views.ListaConvocatoria.as_view()), name='convocatoria_lista'),
    path('convocatoria/nueva', views.nuevo_convocatoria, name='nueva_convocatoria'),
    path('convocatoria/eliminar/<int:id>', views.eliminar_convocatoria, name='eliminar_convocatoria'),
    path('convocatoria/editar/<int:id>', views.editar_convocatoria, name='editar_convocatoria'),
    
    path('presupuesto/', login_required(views_presupuesto.ListaPresupuesto.as_view()), name='presupuesto_lista'),
    path('presupuesto/nuevo', login_required(views_presupuesto.NuevaPresupuestoView.as_view()), name='nuevo_presupuesto'),
    path('presupuesto/editar/<int:pk>', login_required(views_presupuesto.EditarPresupuestoView.as_view()), name='editar_presupuesto'),
    path('presupuesto/eliminar/<int:pk>', login_required(views_presupuesto.EliminarPresupuestoView.as_view()), name='eliminar_presupuesto'),
]
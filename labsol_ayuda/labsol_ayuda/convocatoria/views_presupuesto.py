from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from convocatoria.forms import FormPresupuesto
from convocatoria.models import Convocatoria, Presupuesto
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin



class ListaPresupuesto(ListView):
    model = Presupuesto

class NuevaPresupuestoView(CreateView):
    model = Presupuesto
    form_class = FormPresupuesto
    success_url = reverse_lazy('presupuesto_lista')
    extra_context = {'accion':'Nueva'}

class EditarPresupuestoView(UpdateView):
    model = Presupuesto
    form_class = FormPresupuesto
    extra_context = {'accion':'Modificar'}
    
    success_url = reverse_lazy('presupuesto_lista')
    
class EliminarPresupuestoView(DeleteView):
    model = Presupuesto
    success_url = reverse_lazy('presupuesto_lista')
    
    def form_valid(self, form):
        self.object = self.get_object()
        if Convocatoria.objects.filter(presupuesto=self.object):
            messages.error(self.request, 'No se pode eliminar el presupuesto')
            pass
        else:
            self.object.delete()
            messages.success(self.request, 'Se elimino con éxito el presupuesto disponible')
        
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)  
    
class BienvenidaView(LoginRequiredMixin, TemplateView):
    template_name = 'bienvenida.html'
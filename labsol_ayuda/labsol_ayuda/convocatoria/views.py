from logging import warning
from datetime import date
from pprint import pprint
from django.contrib import messages
from xml.dom import ValidationErr
from django.shortcuts import render, redirect, get_object_or_404
from convocatoria.models import Convocatoria
from django.views.generic import ListView, TemplateView
from convocatoria.forms import FormConvocatoria
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import ValidationError
from django.contrib.messages.views import SuccessMessageMixin



class ListaConvocatoria(ListView):
    model = Convocatoria


def eliminar_convocatoria(request, id):
    conv = get_object_or_404(Convocatoria, id=id)
    conv.delete()
    return redirect('convocatoria_lista')


def nuevo_convocatoria(request):
    if request.method == 'POST':
        form = FormConvocatoria(request.POST)   
        if form.is_valid():
            cierre =request.POST.get("fecha_cierre")
            inicio =request.POST.get("fecha_inicio")
            if cierre < inicio:
                messages.error(request, 'La fecha de cierre no puede ser menor a la fecha de inicio ')
            else:
                form.save()
                return redirect('convocatoria_lista')
            
    else:
        form = FormConvocatoria()
    return render(request, 'nueva_convocatoria.html', {'form':form})


def editar_convocatoria(request, id):
    convocatoria = Convocatoria.objects.get(id=id)
    if request.method == 'POST':
        form = FormConvocatoria(request.POST, instance=convocatoria)
        if form.is_valid():

            cierre =request.POST.get("fecha_cierre")
            inicio =request.POST.get("fecha_inicio")
            if cierre < inicio:
                messages.error(request, 'La fecha de cierre no puede ser menor a la fecha de inicio ')
            else:
              form.save()
              return redirect('convocatoria_lista')
    else:
        form = FormConvocatoria(instance=convocatoria)
    return render(request, 'editar_convocatoria.html', {'form':form})
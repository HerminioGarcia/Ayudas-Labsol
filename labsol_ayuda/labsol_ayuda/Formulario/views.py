from django.shortcuts import render, redirect
from .models import Formularios, ContestaFormularios, DetalleContestaFormularios, Campo, Formularios
from .forms import AplicaFormulario, FormCampos2, FormCampos, FormFormularios, FormFiltroCampo
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.http import HttpResponseRedirect

x = 0 

def formulario(request, id):
    quiz = Formularios.objects.get(id=id)
    form = AplicaFormulario(campos=quiz.campos.all())    
    
    if request.method == 'POST':
        form = AplicaFormulario(request.POST, request.FILES, campos=quiz.campos.all()) 
        if form.is_valid():
            data = form.cleaned_data
            
            contesta_formulario = ContestaFormularios.objects.create(
                formularios = quiz,
                usuario = request.user
            )
            
            for campo in quiz.campos.all():
                DetalleContestaFormularios.objects.create(
                    campo = campo,
                    respuesta = data[f"{campo.campo}"],
                    contesta_formularios = contesta_formulario
                )
        
    context = {
        # 'quiz': quiz,
        'form': form
    }
    
    # Load documents for the list page
    return render(request, 'formulario.html', context)

class NuevoCampoView(CreateView):
    model = Campo
    form_class = FormCampos
    success_url = reverse_lazy('modalidades_lista')
    extra_context = {'accion':'Nueva'}

class ModalidadesCamposLista(ListView):
    model = Campo
    success_url = reverse_lazy('modalidades_lista')
    def get_queryset(self):
        x = 'pk'       
        return  Campo.objects.filter(formularios=self.request.resolver_match.kwargs[x])
    

class CrearFormularioView(CreateView):
    model = Formularios
    form_class = FormFormularios
    success_url = reverse_lazy('modalidades_lista')
    extra_context = {'accion':'Nuevo Formulario'}

class EditarFormularioView(UpdateView):
    model = Formularios
    form_class = FormFormularios
    extra_context = {'accion':'Modificar'}
    success_url = reverse_lazy('modalidades_lista')
    success_message = "Modalidad editada"

def eliminar_formulario(request, id):
    Formularios.objects.get(id=id).delete()
    return redirect('modalidades_lista')
    
class ListaFormulario(ListView):
    model = Formularios

def eliminar_campo(request, id):
    Campo.objects.get(id=id).delete()
    return redirect('modalidades_lista')

class EditarCampoView(UpdateView):
    model = Campo
    form_class = FormCampos
    extra_context = {'accion':'Modificar'}
    success_url = reverse_lazy('modalidades_lista')
    success_message = "Campo editado"

#esto es nuevo

def editar_campo(request, id):
    campo = Campo.objects.get(id=id)
    if request.method == 'POST':
        form = FormCampos2(request.POST, instance=campo)
        if form.is_valid():
            form.save()
            return redirect('modalidades_lista')
    else:
        form = FormCampos2(instance=campo)
    return render(request, 'campo_form.html', {'form':form})

def nuevo_campo(request):
    if request.method == 'POST':
        form = FormCampos2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('modalidades_lista')
    else:
        form = FormCampos2()
    return render(request, 'campo_form.html', {'form':form})


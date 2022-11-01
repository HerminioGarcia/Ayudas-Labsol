from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User, Group
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.views.generic import TemplateView
from django.contrib import messages
from django.views.generic import ListView, TemplateView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required,permission_required
from django.core.paginator import Paginator
from .forms import UserForm, FormDatosPersonales
from .token import token_activacion
from .models import DatosPersonales, Municipio
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

#@login_required

def eliminar_usuario(request, id):
    User = get_user_model()
    User.objects.get(id=id).delete()
    return redirect('usuarios_lista')

class EliminarUsuarioView(DeleteView):
    User = get_user_model()
    model = User
    success_url = reverse_lazy('usuarios_lista')
    
    def form_valid(self, form):
        User = get_user_model()
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, 'Se elimino con éxito el usuario')
        
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)  

class LoginView(LoginView):
    template_name='login.html'
    form_class = AuthenticationForm

class ListaUsuariosView(LoginRequiredMixin,ListView):
    User = get_user_model()
    model = User
    paginate_by= 10
    template_name = 'lista_usuarios.html'

    def get_context_data(self, **kwargs):
        context = super(ListaUsuariosView,self).get_context_data(**kwargs)
        context['grupos'] = Group.objects.all()
        return context

def AsignarGruposUsuario(request):
    id_usuario = request.POST.get('usuario', None)
    User = get_user_model()
    usuario = User.objects.get(id=id_usuario)
    
    usuario.groups.clear()
    for item in request.POST:
        if request.POST[item] == 'on':
            grupo = Group.objects.get(id=int(item))
            usuario.groups.add(grupo)
    messages.success(request, 'Se agregó el usuario a los grupos')
            
    return redirect('usuarios_lista') 

class RegistrarView(SuccessMessageMixin,CreateView):
    model=User
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = "Entre a su correo '%(email)s' para validar su cuenta"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        sitio = get_current_site(self.request)
        
        uid = urlsafe_base64_encode(force_bytes(user.id))
        token = token_activacion.make_token(user)
        mensaje = render_to_string(
            'confirmar_cuenta.html',
            {
                'user': user,
                'sitio': sitio,
                'uid': uid,
                'token': token
            }
        )
        
        asunto = 'Activar cuenta'
        para = user.email
        email = EmailMessage(
            asunto,
            mensaje,
            to=[para],
        )
        email.content_subtype = 'html'
        email.send()
        
        return super().form_valid(form)

class ActivarCuentaView(TemplateView):
    def get(self, request, *args, **kwargs):
        
        try:
            uid = urlsafe_base64_decode(kwargs['uidb64'])
            token = kwargs['token']
            User = get_user_model()
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, User.DoesNotExist):
            user = None
        if user is not None and token_activacion.check_token(user, token):
            user.is_active = True
            user.save()
            
            messages.success(request, 'Cuenta activada, ingresar datos')
        else:
            messages.error(request, 'Token inválido, contacta al administrador')
            
        return redirect('login')

class CrearPerfilView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model=DatosPersonales
    form_class = FormDatosPersonales
    success_url = reverse_lazy('bienvenida')
    success_message = "Datos guardados de manera exitosa"

    def form_valid(self, form):
        datos_personales = form.save(commit=False)
        datos_personales.user = self.request.user
        datos_personales.save()
        
        return super().form_valid(form)
    
class EditarPerfilView(LoginRequiredMixin,UpdateView):
    model=DatosPersonales
    form_class = FormDatosPersonales
    extra_context = {'accion':'Editar'}
    success_url = reverse_lazy('bienvenida')
    success_message = "Datos guardados de manera exitosa"

    def dispatch(self,request,*args,**kwargs):
        self.object=self.get_object()
        return super().dispatch(request,*args,**kwargs)

    def get_object(self,queryset=None):
        return self.request.user.datos

class BienvenidaView(TemplateView):
    template_name = 'bienvenida.html'

def busca_municipios(request):
    id_estado = request.POST.get('id_estado', None)
    if id_estado:
        municipios = Municipio.objects.filter(estado_id=id_estado)
        data = [{'id':mun.id,'nombre':mun.nombre} for mun in municipios]
        return JsonResponse(data, safe=False)
    return JsonResponse({'error':'Parámetro inválido'}, safe=False)  
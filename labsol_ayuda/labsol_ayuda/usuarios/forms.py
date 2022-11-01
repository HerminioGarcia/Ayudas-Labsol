from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .models import DatosPersonales
from django.urls import reverse_lazy

class UserForm(forms.ModelForm):
    repassword = forms.CharField()
    class Meta:
        model=User
        fields=('first_name', 'last_name', 'curp','email','password','repassword')

    def save(self,commit=True):
        user= super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def clean_password(self, *args, **kwargs):
        if self.data['password'] != self.data['repassword']:
            raise forms.ValidationError('Las contraseñas son diferentes; favor de verificar')
        
        return self.data['password']

class FormDatosPersonales(forms.ModelForm):
    class Meta:
        model=DatosPersonales
        exclude = ['user','apoyo']
        widgets = {
            'estado': forms.Select(attrs={
                'class':'form-control',
                'data-url':reverse_lazy('busca_municipios')
            }),
        }
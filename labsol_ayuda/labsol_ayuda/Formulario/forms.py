from django import forms
from django.db import models
from .models import ContestaFormularios, Campo, Formularios
from django.contrib.auth.decorators import login_required,permission_required

class AplicaFormulario(forms.Form):
        
    def __init__(self, *args, **kwargs):
        campos = kwargs.pop('campos')
        
        super(AplicaFormulario, self).__init__(*args, **kwargs)
        
        TIPO_DATO = {
            '1': forms.CharField(max_length=300),
            '2': forms.IntegerField(),
            '3': forms.DecimalField(),
            '4': forms.DateField(widget=forms.DateInput(attrs={'type':'date'})),
            '5': forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime'})),
            '6': forms.EmailField(),
            '7': forms.ModelChoiceField(queryset=None),
            '8': forms.ModelChoiceField(queryset=None, widget=forms.RadioSelect()),
            '9': forms.FileField( )
        }
        for campo in campos:
            self.fields[f"{str(campo.campo)}"] = TIPO_DATO[campo.tipo_dato]
            if campo.tipo_dato in ['7', '8']:
                self.fields[f"{str(campo.campo)}"].queryset = campo.opciones_campo.all()
            if campo.requerida == '0':
                self.fields[f"{str(campo.campo)}"].required = False
            if campo.tipo_dato == '1':
                print (campo.size_texto)
                self.fields[f"{str(campo.campo)}"].max_length = campo.size_texto
                
        # interests = ProfileInterest.objects.filter(
        #     profile=self.instance
        # )
        # for i in range(len(interests) + 1):
        #     field_name = 'interest_%s' % (i,)
        #     self.fields[field_name] = forms.CharField(required=False)
        #     try:
        #         self.initial[field_name] = interests[i].interest
        #     except IndexError:
        #         self.initial[field_name] = “”
        # # create an extra blank field
        # field_name = 'interest_%s' % (i + 1,)
        # self.fields[field_name].queryset = forms.CharField(required=False)

class FormCampos(forms.ModelForm):
    class Meta:
        model = Campo
        fields = '__all__'

class FormCampos2(forms.ModelForm):
    class Meta:
        model = Campo
        exclude = ['formularios']

class FormFormularios(forms.ModelForm):
    class Meta:
        model = Formularios
        fields = '__all__'

class FormFiltroCampo(forms.Form):
    campo = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}),
        required=False
    )   
    descripcion = forms.CharField( 
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Descripción'}),
        required=False
    )   
    tipo_dato = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Tipo de dato'}),
        required=False
    )   
    formularios = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'formularios'}),
        required=False
    )   
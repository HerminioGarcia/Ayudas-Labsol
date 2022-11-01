from dataclasses import fields
from django import forms
from convocatoria.models import Convocatoria, Presupuesto


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class FormConvocatoria(forms.ModelForm):
        
    class Meta:
        model = Convocatoria
        fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_inicio': DateInput(),
            'hora_inicio': TimeInput(),
            'fecha_cierre': DateInput(),
            'hora_cierre': TimeInput(),
        }
        
class FormPresupuesto(forms.ModelForm):
        
    class Meta:
        model = Presupuesto
        fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            
        }
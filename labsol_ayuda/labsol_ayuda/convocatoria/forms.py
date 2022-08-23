from dataclasses import fields
from django import forms
from convocatoria.models import Convocatoria, Presupuesto

class FormConvocatoria(forms.ModelForm):
        
    class Meta:
        model = Convocatoria
        fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'decripcion': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            'apoyo': forms.Select(attrs={'class':'form-control'}),
            'presupuesto': forms.Select(attrs={'class':'form-control'}),
            
        }
        
class FormPresupuesto(forms.ModelForm):
        
    class Meta:
        model = Presupuesto
        fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            
        }
from django import forms
from .models.cliente import cliente
from .models.producto import producto

class clienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'
        
class productoForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'
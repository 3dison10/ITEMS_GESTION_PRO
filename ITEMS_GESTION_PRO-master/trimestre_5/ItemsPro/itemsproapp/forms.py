from django import forms
from .models.cliente import cliente
from .models.producto import producto
from .models.registro import registro

class clienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'
        
class productoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = registro
        fields = '__all__'

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import cliente
from .forms import clienteForm

# Create your views here.

def home(request):
    return render(request, 'paginas/home.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')

def usuarios(request):
    usuarios = cliente.objects.all()
    return render(request, 'usuarios/clientesLista.html', {'usuarios':usuarios})  

def crear(request):
    formulario = clienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('usuarios')
    return render(request, 'usuarios/crearCliente.html', { 'formulario':formulario} )

def productos(request):
    return render(request, 'usuarios/productos.html')

def editar(request, id):
    clienteEditado = cliente.objects.get(id=id)
    formulario = clienteForm(request.POST or None, request.FILES or None, instance=clienteEditado)
    
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('usuarios')
    
    return render(request, 'usuarios/editar.html', { 'formulario':formulario} )

def borrar(request, id):
    clienteBorrado = cliente.objects.get(id=id)
    clienteBorrado.delete()
    return redirect('usuarios')


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models.cliente import cliente
from .models.producto import producto
from .forms import clienteForm
from .forms import productoForm

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
    productos = producto.objects.all()
    print(productos)
    return render(request, 'productos/indexProd.html', {'productos':productos})

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

def crearProd (request):
    formulario = productoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request, 'productos/crearProd.html', { 'formulario':formulario})

def editarProd (request, id):
    productoEditado = producto.objects.get(id=id)
    formulario = productoForm(request.POST or None, request.FILES or None, instance=productoEditado)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('productos')
    
    return render(request, 'productos/editarProd.html',{ 'formulario':formulario})

def borrarProd(request, id):
    prodBorrado = cliente.objects.get(id=id)
    prodBorrado.delete()
    return redirect('productos')


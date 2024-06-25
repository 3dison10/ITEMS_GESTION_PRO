from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models.cliente import cliente
from .models.producto import producto
from .forms import clienteForm, productoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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
    prodForm = productoForm(request.POST or None, request.FILES or None)
    if prodForm.is_valid():
        prodForm.save()
        return redirect('productos')
    return render(request, 'productos/crearProd.html', { 'formProd':prodForm})

def editarProd (request, idProd):
    productoEditado = producto.objects.get(idProd=idProd)
    prodForm = productoForm(request.POST or None, request.FILES or None, instance=productoEditado)
    if prodForm.is_valid() and request.POST:
        prodForm.save()
        return redirect('productos')
    
    return render(request, 'productos/editarProd.html',{ 'formProd':prodForm})

def borrarProd(request, idProd):
    prodBorrado = get_object_or_404(producto, idProd=idProd)
    prodBorrado.delete()
    return redirect('productos')

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
	else:
		form = UserCreationForm()

	context = { 'form' : form }
	return render(request, 'usuarios/register.html', context)   


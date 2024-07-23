from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name='home'), 
    path('usuarios/homeAdmin/', views.home_admin, name='home_admin'), 
    path('contacto/', views.contacto, name='contacto'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuarios/crearCliente/', views.crear, name='crear_cliente'),
    path('productos/', views.productos, name='productos'),
    path('usuarios/editar/<int:id>/', views.editar, name='editar_usuario'),
    path('borrar/<int:id>/', views.borrar, name='borrar_usuario'),
    path('productos/crearProd/', views.crearProd, name='crearProd'),  # Asegúrate de que esta línea esté correcta
    path('productos/editarProd/<int:idProd>/', views.editarProd, name='editarProd'),
    path('productos/borrarProd/<int:idProd>/', views.borrarProd, name='borrarProd'),
    path('salir/', views.salir, name='salir'),
    path('accounts/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
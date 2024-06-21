from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name='home'), 
    path('contacto/', views.contacto, name='contacto'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuarios/crearCliente/', views.crear, name='crear'),
    path('usuarios/productos/', views.productos, name='productos'),
    path('usuarios/editar/', views.editar, name='editar'),
    path('borrar/<int:id>', views.borrar, name='borrar'),
    path('usuarios/editar/<int:id>', views.editar, name='editar'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from .models import cliente
from .models import producto


# Register your models here.

admin.site.register(cliente)
admin.site.register(producto)

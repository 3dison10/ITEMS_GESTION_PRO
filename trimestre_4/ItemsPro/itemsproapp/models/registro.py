from django.db import models

class registro(models.Model):

    idEdif = models.AutoField(primary_key=True)
    nitEdif = models.CharField(max_length=12, verbose_name="NIT.")
    nombreEdif = models.CharField(max_length=30, unique=True)
    direccionEdif = models.CharField(max_length=50)
    nombreProp = models.CharField(max_length=50)
    emailAdmon = models.EmailField(unique=True)

    # Campos booleanos
    esta_activa = models.BooleanField(default=True)
    es_personal = models.BooleanField(default=False)

    # Campos con opciones
    OPCIONES_ROL = [
        ('usuario', 'Propietario'),
        ('admin', 'Administrador'),
    ]
    roles = models.CharField(max_length=7, choices=OPCIONES_ROL, default='usuario')

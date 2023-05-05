from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombres")
    apellidos = models.CharField(max_length=150, verbose_name="Apellidos")
    empresa = models.CharField(max_length=150, verbose_name="Empresa")
    rif = models.CharField(max_length=10, unique=True, verbose_name="RIF")
    tlf = models.CharField(max_length=11, verbose_name="Telefono")
    user = models.CharField(max_length=12, unique=True, verbose_name="Usuario")
    email = models.EmailField(max_length=150, unique=True, verbose_name="Correo")
    password = models.CharField(max_length=8, unique=True, verbose_name="Contraseña")
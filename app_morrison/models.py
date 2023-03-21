from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=15)
    correo = models.EmailField(max_length=50)
    contrasenia = models.PasswordField(max_length=50)
    def __str__(self):
        return self.nombre

class Pedidos(models.Model):
    mapa = models.CharField(max_length=50)
    caracteristicas = models.TextField(max_length=10000)
    def __str__(self):
        return self.mapa

class Personal(models.Model):
    nombre = models.CharField(max_length=15)
    correo = models.EmailField(max_length=50)
    contrasenia = models.PasswordField(max_length=50)
    def __str__(self):
        return self.nombre
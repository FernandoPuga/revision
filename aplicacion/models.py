from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Carpinteros(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    localidad = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"



class Electricistas(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    localidad = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
 
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    

class Plomeros(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    localidad = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    

class Gasistas(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    localidad = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    matricula = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    

class Pintores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    localidad = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
from django.db import models

# Create your models here.

class Carpinteros(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.IntegerField()
    localidad = models.CharField(max_length=50)




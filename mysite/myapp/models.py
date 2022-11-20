from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.CharField(max_length=200)
    fechaNac = models.DateTimeField('Fecha de Nacimiento')
    


from django.db import models

# Create your models here.

class Ciudadano(models.Model):

    nombre= models.CharField(max_length=40) #str corto
    edad=models.IntegerField() #numero entero
    ciudad = models.CharField(max_length=40) # str corto
    

class Dispositivos(models.Model): 
    
    celular = models.CharField(max_length=40) #str corto
    computadora =models.CharField(max_length=40) # str corto
    tablet =models.CharField(max_length=40) #numero entero

class Tiempo (models.Model): 

    dias = models.IntegerField() #numero corto
    horas = models.IntegerField() #numero entero

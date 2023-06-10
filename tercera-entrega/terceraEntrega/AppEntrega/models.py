from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
    def __str__(self):
        return f"Curso: {self.nombre} - Camada: {self.camada}"

class Entrenador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Socio(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    dni = models.IntegerField()
    num_socio = models.IntegerField()
    
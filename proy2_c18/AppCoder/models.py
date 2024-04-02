from django.db import models

# Create your models here.
class Curso (models.Model):
    nombre =models.CharField(max_length=40)
    camada= models.IntegerField()


class Alumno (models.Model):
    nombre =models.CharField(max_length=40)
    dni = models.IntegerField()
    grupo = models.CharField(max_length=40)

class Profesor (models.Model):
    nombre =models.CharField(max_length=40)
    dni = models.IntegerField()
    grupo = models.CharField(max_length=40)


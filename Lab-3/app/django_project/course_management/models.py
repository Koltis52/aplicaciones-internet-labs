from django.db import models

# Create your models here.
class Asignaturas(models.Model):
    nombre = models.CharField(max_lenght=30)
    codigo = models.IntegerField()
    
class Alumnos(models.Model):
    nombre = models.CharField(max_lenght=30)
    apellido_paterno = models.CharField(max_lenght=30)
    apellido_materno = models.CharField(max_lenght=30)
    fecha_de_nacimiento = models.DateField()
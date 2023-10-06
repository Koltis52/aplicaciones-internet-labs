from django.shortcuts import render
from .models import Asignaturas, Alumnos

def index(request):
    asignaturas = Asignaturas.objects.all()
    return render(request, 'index.html', {'asignaturas':asignaturas})

def crear_asignatura(request):
    return render(request, 'crear_asignatura.html')

def agregar_asignatura(request):
    return render(request, 'guardar_asignatura.py')
from django.shortcuts import render
from .models import Asignaturas, Alumnos
from .forms import AsignaturaForm
from django.http import HttpResponseRedirect

def index(request):
    asignaturas = Asignaturas.objects.all()
    return render(request, 'index.html', {'asignaturas':asignaturas})

def crear_asignatura(request):
    form = AsignaturaForm(request.POST)
    return render(request, 'crear_asignatura.html',{'form': form})

def guardar_asignatura(request):
    form = AsignaturaForm(request.POST)
    asignaturas = Asignaturas.objects.all()
    return render(request, 'index.html', {'asignaturas':asignaturas})
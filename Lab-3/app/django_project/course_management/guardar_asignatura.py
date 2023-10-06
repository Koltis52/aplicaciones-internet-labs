from .models import Asignaturas, Alumnos
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm

def agregar_asignatura(request):
    form = NameForm(request.POST)
    b = Asignaturas(nombre=form.nombre_asignatura, codigo=form.codigo_asignatura)
    b.save()
    #return HttpResponseRedirect("/thanks/")
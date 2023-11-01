import json
from django.shortcuts import render
from .models import Asignaturas, Alumnos
from .forms import AsignaturaForm, AlumnoForm
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    asignaturas = Asignaturas.objects.all()
    return render(request, 'index.html', {'asignaturas':asignaturas})

def crear_asignatura(request):
    if request.method == "POST":
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            b = Asignaturas(
                nombre=form.cleaned_data['nombre_asignatura'], 
                codigo=form.cleaned_data['codigo_asignatura'])
            b.save()
            return HttpResponseRedirect("http://localhost:8080/")
    else:
        form = AsignaturaForm()
    return render(request, 'crear_asignatura.html',{'form': form})

def eliminar_asignatura(request):
    body_data = json.loads(request.body)
    Asignaturas.objects.filter(nombre=body_data).delete()
    return True

def asignatura_eliminada(request):
    return render(request, 'asignatura_eliminada.html')

def crear_alumnos(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            b = Alumnos(
                nombre=form.cleaned_data['nombre_alumno'], 
                apellido_paterno=form.cleaned_data['apellido_paterno'],
                apellido_materno=form.cleaned_data['apellido_materno'],
                fecha_de_nacimiento=form.cleaned_data['fecha_de_nacimiento'])
            b.save()
            return HttpResponseRedirect("http://localhost:8080/")
    else:
        form = AlumnoForm()
    return render(request, 'crear_alumnos.html',{'form': form})
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

def modificar_asignatura(request, nombre_a):
    form = AsignaturaForm(request.POST)
    if form.is_valid():
        b = Asignaturas.objects.get(nombre=nombre_a)
        b.nombre = form.cleaned_data['nombre_asignatura']
        b.codigo = form.cleaned_data['codigo_asignatura']
        b.save()
        return HttpResponseRedirect("http://localhost:8080/")
    else:
        form = AsignaturaForm()
    return render(request, 'modificar_asignatura.html',{'form': form})

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

def agregar_alumnos(request, nombre_a):
    if request.method == "POST":
        for element in request.POST.getlist('lista_alumnos'):
            b = Alumnos.objects.get(nombre=element)
            c = Asignaturas.objects.get(nombre=nombre_a)
            c.alumnos.add(b)
        return HttpResponseRedirect("http://localhost:8080/")
    else:
        alumnos = Alumnos.objects.all()
    return render(request, 'agregar_alumnos.html', {'alumnos':alumnos})

def modificar_alumnos(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'modificar_alumnos.html', {'alumnos':alumnos})

def modificar_alumno(request, nombre_a):
    form = AlumnoForm(request.POST)
    if form.is_valid():
        b = Alumnos.objects.get(nombre=nombre_a)
        b.nombre = form.cleaned_data['nombre_alumno']
        b.apellido_paterno = form.cleaned_data['apellido_paterno']
        b.apellido_materno = form.cleaned_data['apellido_materno']
        b.fecha_de_nacimiento = form.cleaned_data['fecha_de_nacimiento']
        b.save()
        return HttpResponseRedirect("http://localhost:8080/modificar alumnos/")
    else:
        form = AlumnoForm()
    return render(request, 'modificar_alumno.html',{'form': form})

def quitar_alumnos(request, nombre_a):
    if request.method == "POST":
        for element in request.POST.getlist('lista_alumnos'):
            b = Alumnos.objects.get(nombre=element)
            c = Asignaturas.objects.get(nombre=nombre_a)
            c.alumnos.remove(b)
        return HttpResponseRedirect("http://localhost:8080/")
    else:
        b = Asignaturas.objects.get(nombre=nombre_a)
        alumnos = b.alumnos.all()
    return render(request, 'quitar_alumnos.html', {'alumnos':alumnos})


def eliminar_alumno(request):
    if request.method == "POST":
        body_data = json.loads(request.body)
        Alumnos.objects.filter(nombre=body_data).delete()
        return True
    else:
        alumnos = Alumnos.objects.all()
    return render(request, 'eliminar_alumno.html', {'alumnos':alumnos})
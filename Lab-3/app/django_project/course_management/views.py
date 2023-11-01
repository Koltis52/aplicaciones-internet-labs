import json
from django.shortcuts import render
from .models import Asignaturas, Alumnos
from .forms import AsignaturaForm
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    asignaturas = Asignaturas.objects.all()
    return render(request, 'index.html', {'asignaturas':asignaturas})

def crear_asignatura(request):
    if request.method == "POST":
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            b = Asignaturas(nombre=form.cleaned_data['nombre_asignatura'], codigo=form.cleaned_data['codigo_asignatura'])
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
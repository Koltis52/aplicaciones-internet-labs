from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
	return render(request, 'index.html')

def crear_asignatura(request):
    return render(request, 'crear_asignatura.html')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
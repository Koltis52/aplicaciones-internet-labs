from django.shortcuts import render
from .models import Course, Student
from django.http import HttpResponse
import requests

def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html',{'courses':courses})

def peticion_random(request):
    url = "https://moviesdatabase.p.rapidapi.com/titles/random"

    querystring = {"list":"top_rated_series_250"}

    headers = {
	    "X-RapidAPI-Key": "6ab30a3e29msh99f48e91eab357cp14a8e5jsnedab8a8b1c24",
	    "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    datas = response.json

    return render(request, 'index.html', {'datas':datas})
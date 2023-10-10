from django.shortcuts import render
import requests

def index(request):
    url = "http://api.filmon.com/api/vod/genres"

    response = requests.get(url)

    datas = response.json

    return render(request, 'index.html', {'datas':datas})

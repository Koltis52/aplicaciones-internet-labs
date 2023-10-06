from django.urls import path

from . import views

urlpatterns = [
    path('crear asignatura/', views.crear_asignatura),
    path('', views.index, name="index"),
]
from django.urls import path

from . import views

urlpatterns = [
    path('eliminar asignatura/', views.eliminar_asignatura),
    path('asignatura eliminada/', views.asignatura_eliminada),
    path('crear asignatura/', views.crear_asignatura),
    path('', views.index, name="index"),
]
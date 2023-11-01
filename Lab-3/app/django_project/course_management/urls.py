from django.urls import path

from . import views

urlpatterns = [
    path('eliminar asignatura/', views.eliminar_asignatura),
    path('asignatura eliminada/', views.asignatura_eliminada),
    path('crear asignatura/', views.crear_asignatura),
    path('modificar asignatura/<nombre_a>/', views.modificar_asignatura),
    path('agregar alumnos/<nombre_a>/', views.agregar_alumnos),
    path('modificar alumnos/', views.modificar_alumnos),
    path('modificar alumno/<nombre_a>', views.modificar_alumno),
    path('quitar alumnos/<nombre_a>', views.quitar_alumnos),
    path('eliminar alumno/', views.eliminar_alumno),
    path('crear alumnos/', views.crear_alumnos),
    path('', views.index, name="index"),
]
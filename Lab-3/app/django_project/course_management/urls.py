from django.urls import path

from . import views

urlpatterns = [
    path('xd/', views.current_datetime),
    path('crear asignatura/', views.crear_asignatura),
    path('', views.index, name="index"),
]
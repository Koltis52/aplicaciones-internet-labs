from django.urls import path

from . import views

urlpatterns = [
    path('random/', views.peticion_random, name='random'),
    path('', views.index, name="index"),
]
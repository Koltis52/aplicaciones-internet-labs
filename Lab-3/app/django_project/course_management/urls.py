from django.urls import path

from . import views

urlpatterns = [
    path('xd/', views.current_datetime),
    path('', views.index, name="index"),
]
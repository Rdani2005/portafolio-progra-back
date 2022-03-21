from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="Rutas"),
    path('enunciados/', views.getEnunciados, name="Enunciados"),
    path('enunciados/enunciado/<str:pk>/', views.getEnunciado, name='Enunciado'),
]
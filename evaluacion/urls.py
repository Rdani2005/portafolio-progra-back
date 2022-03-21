from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="Rutas"),
    path('evaluaciones/', views.getEvaluaciones, name="Enunciados"),
    path('evaluaciones/evaluacion/<str:pk>/', views.getEvaluacion, name='Enunciado'),
]
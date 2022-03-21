from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="Rutas"),
    path('complementarios/', views.getComplementarios, name="complementarios"),
    path('complementarios/complementario/<str:pk>/', views.getComplementario, name='Complementario'),
]
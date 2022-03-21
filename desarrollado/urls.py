from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="Rutas"),
    path('desarrollados/', views.getDesarrollados, name="complementarios"),
    path('desarrollados/desarrollado/<str:pk>/', views.getDesarrollado, name='Complementario'),
]
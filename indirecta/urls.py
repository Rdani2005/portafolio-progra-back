from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="Rutas"),
    path('indirectas/', views.getIndirectas, name="Indirectas"),
    path('indirectas/indirecta/<str:pk>/', views.getIndirecta, name='Indirecta'),
]
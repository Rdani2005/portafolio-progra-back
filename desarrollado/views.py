from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# My own files
from .models import Trabajos
from .serializers import TrabajosSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'endpoint':'/desarrollados/',
            'methods': 'GET',
            'body': None,
            'Description': 'Regresa un arreglo de todos los trabajos realizados'
        },
        {
            'endpoint': '/desarrollados/desarrollado/id/',
            'methods': 'GET',
            'body': None,
            'Description': 'Regresa un arreglo de la trabajo realizado'
        }

    ]
    return Response(routes)

@api_view(['GET'])
def getDesarrollados(request):
    desarrollado = Trabajos.objects.all().order_by('-publicado')
    serializer = TrabajosSerializer(desarrollado, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDesarrollado(request, pk):
    desarrollado = Trabajos.objects.get(id=pk)
    serializer = TrabajosSerializer(desarrollado, many=False)
    return Response(serializer.data)

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# My own files
from .models import Enunciados
from .serializers import EnunciadosSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'endpoint':'/enunciados/',
            'methods': 'GET',
            'body': None,
            'Description': 'Regresa un arreglo de todos los enunciados'
        },
        {
            'endpoint': '/enunciados/enunciado/id/',
            'methods': 'GET',
            'body': None,
            'Description': 'Regresa un arreglo del enunciado solicitado'
        }

    ]
    return Response(routes)

@api_view(['GET'])
def getEnunciados(request):
    enunciados = Enunciados.objects.all().order_by('-publicado')
    serializer = EnunciadosSerializer(enunciados, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEnunciado(request, pk):
    enunciado = Enunciados.objects.get(id=pk)
    serializer = EnunciadosSerializer(enunciado, many=False)
    return Response(serializer.data)

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# My own files
from .models import Indirecta
from .serializers import IndirectaSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'endpoint':'/indirectas/',
            'methods': 'GET',
            'body': None,
            'Description': 'Regresa un arreglo de todas los archivos indirectos'
        },
        {
            'endpoint': '/indirectas/indirecta/id/',
            'methods': 'GET',
            'body': None,
            'Description': 'Regresa un arreglo del archivo indirecto solicitado'
        }

    ]
    return Response(routes)

@api_view(['GET'])
def getIndirectas(request):
    indirectas = Indirecta.objects.all().order_by('-publicado')
    serializer = IndirectaSerializer(indirectas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getIndirecta(request, pk):
    indirecta = Indirecta.objects.get(id=pk)
    serializer = IndirectaSerializer(indirecta, many=False)
    return Response(serializer.data)

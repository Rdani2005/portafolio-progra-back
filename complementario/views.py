from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# My own files
from .models import Complementarios
from .serializers import ComplementariosSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'endpoint':'/complementarios/',
            'methods': 'GET',
            'body': None,
            'Description': 'Regresa un arreglo de todos las actividades complementarias hechas'
        },
        {
            'endpoint': '/complementarios/conplementario/id',
            'methods': 'GET',
            'body': None,
            'Description': 'Regresa un arreglo de la actividad realizada'
        }

    ]
    return Response(routes)

@api_view(['GET'])
def getComplementarios(request):
    complementarios = Complementarios.objects.all().order_by('-publicado')
    serializer = ComplementariosSerializer(complementarios, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getComplementario(request, pk):
    complementario = Complementarios.objects.get(id=pk)
    serializer = ComplementariosSerializer(complementario, many=False)
    return Response(serializer.data)
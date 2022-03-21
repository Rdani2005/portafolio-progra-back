from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# My own files
from .models import Evaluacion
from .serializers import EvaluacionSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'endpoint':'/evaluaciones/',
            'methods': 'GET',
            'body': None,
            'Description': 'Regresa un arreglo de todas las evaluaciones'
        },
        {
            'endpoint': '/evaluaciones/evaluacion/id/',
            'methods': 'GET',
            'body': None,
            'Description': 'Regresa un arreglo de la evaluacion solicitada'
        }

    ]
    return Response(routes)

@api_view(['GET'])
def getEvaluaciones(request):
    evaluaciones = Evaluacion.objects.all().order_by('-publicado')
    serializer = EvaluacionSerializer(evaluaciones, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEvaluacion(request, pk):
    evaluacion = Evaluacion.objects.get(id=pk)
    serializer = EvaluacionSerializer(evaluacion, many=False)
    return Response(serializer.data)


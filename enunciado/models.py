from django.db import models

# Create your models here.

class Enunciados(models.Model):
    PROJECT = 'PROJECT'
    COTIDIANOS = 'COTIDIANOS'
    TAREAS = 'TAREAS'

    CHOICES_TYPE = [
        (PROJECT, 'Proyecto'),
        (COTIDIANOS, 'Cotidianos'),
        (TAREAS, 'Tareas'),
    ]
    
    titulo = models.CharField(max_length=50)
    tipo_enunciado = models.CharField(
        max_length=10, choices=CHOICES_TYPE, default=COTIDIANOS)

    descripcion = models.TextField()
    publicado = models.DateTimeField(auto_now_add=True)

    def is_upperclass(self):
        return self.tipo_enunciado in {self.COTIDIANOS, self.TAREAS}

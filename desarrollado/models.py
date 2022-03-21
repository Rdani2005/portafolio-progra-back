from django.db import models

# Create your models here.
class Trabajos(models.Model):
    PROJECT = 'PROJECT'
    COTIDIANOS = 'COTIDIANOS'
    TAREAS = 'TAREAS'

    CHOICES_TYPE = [
        (PROJECT, 'Proyecto'),
        (COTIDIANOS, 'Cotidianos'),
        (TAREAS, 'Tareas'),
    ]
    
    titulo = models.CharField(max_length=50)
    direccion_imagen = models.TextField()
    tipo_trabajo = models.CharField(
        max_length=10, choices=CHOICES_TYPE, default=COTIDIANOS)

    descripcion = models.TextField()
    direccion = models.TextField()
    publicado = models.DateTimeField(auto_now_add=True)

    def is_upperclass(self):
        return self.tipo_trabajo in {self.COTIDIANOS, self.TAREAS}

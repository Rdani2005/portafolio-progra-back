from django.db import models

class Complementarios(models.Model):
    PROYECTO = 'PROYECTO'
    DIAGNOSTICO = 'DIAGNOSTICO'

    CHOICES_TYPE = [
        (PROYECTO, 'Trabajo Escrito del Proyecto'),
        (DIAGNOSTICO, 'Diagnostico Aplicado'),
    ]
    
    titulo = models.CharField(max_length=50)
    direccion_imagen = models.TextField()
    tipo_trabajo = models.CharField(
        max_length=20, choices=CHOICES_TYPE, default=PROYECTO)

    descripcion = models.TextField()
    direccion = models.TextField()
    publicado = models.DateTimeField(auto_now_add=True)

    def is_upperclass(self):
        return self.tipo_trabajo in {self.PROYECTO, self.DIAGNOSTICO}


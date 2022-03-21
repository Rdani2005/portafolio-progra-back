from django.db import models

class Evaluacion(models.Model):
    EXAMEN = 'EXAMEN'
    COTEJO = 'COTEJO'
    TAREAS = 'TAREAS'

    CHOICES_TYPE = [
        (EXAMEN, 'Examen Desarrollado'),
        (COTEJO, 'Cotejo'),
    ]
    
    titulo = models.CharField(max_length=50)
    direccion_imagen = models.TextField()
    tipo_trabajo = models.CharField(
        max_length=10, choices=CHOICES_TYPE, default=COTEJO)

    descripcion = models.TextField()
    direccion = models.TextField()
    publicado = models.DateTimeField(auto_now_add=True)

    def is_upperclass(self):
        return self.tipo_trabajo in {self.EXAMEN, self.COTEJO}


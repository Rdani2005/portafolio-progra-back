from django.db import models

class Indirecta(models.Model):
    EXAMEN = 'EXAMEN'
    MATERIAL = 'MATERIAL'
    ADICIONAL = 'ADICIONAL'

    CHOICES_TYPE = [
        (EXAMEN, 'Temario de Examen'),
        (MATERIAL, 'Material de Clase'),
        (ADICIONAL, 'Material Adicional'),
    ]
    
    titulo = models.CharField(max_length=50)
    direccion_imagen = models.TextField()
    tipo_trabajo = models.CharField(
        max_length=20, choices=CHOICES_TYPE, default=MATERIAL)

    descripcion = models.TextField()
    direccion = models.TextField()
    publicado = models.DateTimeField(auto_now_add=True)

    def is_upperclass(self):
        return self.tipo_trabajo in {self.EXAMEN, self.MATERIAL}


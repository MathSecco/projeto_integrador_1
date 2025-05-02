from django.db import models

# Create your models here.
from django.db import models

class Reproducao(models.Model):
    animal_id = models.CharField(max_length=50)
    data = models.DateField()
    tipo_evento = models.CharField(max_length=50, choices=[
        ('cio', 'Cio'),
        ('inseminacao', 'Inseminação'),
        ('cobertura', 'Cobertura Natural'),
        ('gestacao_confirmada', 'Gestação Confirmada'),
        ('parto', 'Parto')
    ])
    detalhes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Evento reprodutivo ({self.tipo_evento}) - {self.animal_id} em {self.data}"

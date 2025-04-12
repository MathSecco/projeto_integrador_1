from django.db import models

# Create your models here.

from django.db import models

class Ordenha(models.Model):
    animal_id = models.CharField(max_length=50)
    data = models.DateField()
    quantidade_leite = models.DecimalField(max_digits=5, decimal_places=2)
    periodo = models.CharField(max_length=20, choices=[('manhã', 'Manhã'), ('tarde', 'Tarde')])
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Ordenha do animal {self.animal_id} em {self.data}"

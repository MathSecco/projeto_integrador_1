from django.db import models

class Alimentacao(models.Model):
    animal_id = models.CharField(max_length=50)
    data = models.DateField()
    tipo_alimento = models.CharField(max_length=100)
    quantidade = models.DecimalField(max_digits=5, decimal_places=2)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Alimentação do animal {self.animal_id} em {self.data}"

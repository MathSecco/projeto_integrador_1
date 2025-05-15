from django.db import models
from django.contrib.auth.models import User

class Alimentacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alimentacao")
    animal_id = models.CharField(max_length=50)
    data = models.DateField()
    tipo_alimento = models.CharField(max_length=100)
    quantidade = models.DecimalField(max_digits=5, decimal_places=2)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Alimentação do animal {self.animal_id} em {self.data}"

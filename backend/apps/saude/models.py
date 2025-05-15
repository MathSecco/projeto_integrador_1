from django.db import models
from django.contrib.auth.models import User

class Saude(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="saude")
    animal_id = models.CharField(max_length=50)
    data = models.DateField()
    tipo_atendimento = models.CharField(max_length=100)  # vacinação, vermífugo, etc
    medicamento = models.CharField(max_length=100, blank=True, null=True)
    responsavel = models.CharField(max_length=100)  # quem aplicou
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Atendimento de saúde para o animal {self.animal_id} em {self.data}"

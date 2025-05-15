from django.db import models
from django.contrib.auth.models import User

class Saude(models.Model):
    TIPO_ATENDIMENTO = (
        ("vacina", "Vacinação"),
        ("vermifugo", "Vermifugação"),
        ("doenca", "Tratamento de doença"),
        ("outros", "Outros"),
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=30, choices=TIPO_ATENDIMENTO)
    data = models.DateField()
    descricao = models.TextField(blank=True)
    proxima_dose = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.usuario} - {self.tipo} ({self.data})"

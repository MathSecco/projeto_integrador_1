from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    nome_completo = models.CharField(max_length=255)
    nome_social = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=20)
    cpf_cnpj = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='perfil_fotos/', blank=True, null=True)  # 🆕

    def __str__(self):
        return self.nome_completo or self.user.username

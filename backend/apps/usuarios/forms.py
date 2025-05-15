from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class RegistroForm(UserCreationForm):
    email = forms.EmailField()
    nome_completo = forms.CharField()
    nome_social = forms.CharField(required=False)
    telefone = forms.CharField()
    cpf_cnpj = forms.CharField()
    endereco = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',
                  'nome_completo', 'nome_social', 'telefone', 'cpf_cnpj', 'endereco']

    def save(self, commit=True):
        user = super().save(commit)
        perfil = user.perfil
        perfil.nome_completo = self.cleaned_data['nome_completo']
        perfil.nome_social = self.cleaned_data['nome_social']
        perfil.telefone = self.cleaned_data['telefone']
        perfil.cpf_cnpj = self.cleaned_data['cpf_cnpj']
        perfil.endereco = self.cleaned_data['endereco']
        perfil.save()
        return user

class PerfilForm(forms.ModelForm):
    nome_completo = forms.CharField()
    nome_social = forms.CharField(required=False)
    telefone = forms.CharField()
    cpf_cnpj = forms.CharField()
    endereco = forms.CharField()
    foto = forms.ImageField(required=False)  # 🆕

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(self.instance, 'perfil'):
            self.fields['nome_completo'].initial = self.instance.perfil.nome_completo
            self.fields['nome_social'].initial = self.instance.perfil.nome_social
            self.fields['telefone'].initial = self.instance.perfil.telefone
            self.fields['cpf_cnpj'].initial = self.instance.perfil.cpf_cnpj
            self.fields['endereco'].initial = self.instance.perfil.endereco

    def save(self, commit=True):
        user = super().save(commit)
        perfil = user.perfil
        perfil.nome_completo = self.cleaned_data['nome_completo']
        perfil.nome_social = self.cleaned_data['nome_social']
        perfil.telefone = self.cleaned_data['telefone']
        perfil.cpf_cnpj = self.cleaned_data['cpf_cnpj']
        perfil.endereco = self.cleaned_data['endereco']
        perfil.foto = self.cleaned_data.get('foto') or perfil.foto
        if commit:
            perfil.save()
        return user
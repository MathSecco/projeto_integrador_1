from django import forms
from .models import Reproducao

class ReproducaoForm(forms.ModelForm):
    class Meta:
        model = Reproducao
        exclude = ['usuario']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'tipo': forms.TextInput(),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }

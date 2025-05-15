from django import forms
from .models import Alimentacao

class AlimentacaoForm(forms.ModelForm):
    class Meta:
        model = Alimentacao
        exclude = ['usuario']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'quantidade': forms.NumberInput(attrs={
                'step': '0.01',
                'inputmode': 'decimal',
                'placeholder': 'Kg (ex: 12.5)'
            }),
            'tipo_alimento': forms.TextInput(),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }

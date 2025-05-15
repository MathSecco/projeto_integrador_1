from django import forms
from .models import Ordenha

class OrdenhaForm(forms.ModelForm):
    class Meta:
        model = Ordenha
        exclude = ['usuario']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'quantidade_leite': forms.NumberInput(attrs={
                'step': '0.01',             # ✅ permite decimais
                'inputmode': 'decimal',     # ✅ mobile-friendly
                'placeholder': 'Litros (ex: 12.5)'  # opcional
            }),
            'periodo': forms.Select(),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }

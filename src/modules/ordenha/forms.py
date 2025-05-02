from django import forms
from .models import Ordenha

class OrdenhaForm(forms.ModelForm):
    class Meta:
        model = Ordenha
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'quantidade_leite': forms.NumberInput(attrs={'step': '0.01'}),
            'periodo': forms.Select(),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }

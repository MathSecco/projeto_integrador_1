from django import forms
from .models import Saude

class SaudeForm(forms.ModelForm):
    class Meta:
        model = Saude
        exclude = ['usuario']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }

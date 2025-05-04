from django import forms
from .models import Saude

class SaudeForm(forms.ModelForm):
    class Meta:
        model = Saude
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }

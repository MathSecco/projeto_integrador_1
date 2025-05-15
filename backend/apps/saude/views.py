from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SaudeForm

def registrar_saude(request):
    form = SaudeForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        saude = form.save(commit=False)
        saude.usuario = request.user
        saude.save()
        messages.success(request, 'Saúde registrada com sucesso!')
        return redirect('registrar_saude')

    return render(request, 'form_base.html', {
        'form': form,
        'titulo': 'Registro de Saúde',
    })

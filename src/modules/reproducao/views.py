from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReproducaoForm

def registrar_reproducao(request):
    form = ReproducaoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Reprodução registrada com sucesso!')
        return redirect('registrar_reproducao')

    return render(request, 'form_base.html', {
        'form': form,
        'titulo': 'Registro de Reprodução',
    })

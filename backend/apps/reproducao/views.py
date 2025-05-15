from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ReproducaoForm

@login_required
def registrar_reproducao(request):
    form = ReproducaoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        reproducao = form.save(commit=False)
        reproducao.usuario = request.user
        reproducao.save()
        messages.success(request, 'Reprodução registrada com sucesso!')
        return redirect('registrar_reproducao')

    return render(request, 'form_base.html', {
        'form': form,
        'titulo': 'Registro de Reprodução',
    })

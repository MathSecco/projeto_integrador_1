from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AlimentacaoForm

@login_required
def registrar_alimentacao(request):
    form = AlimentacaoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        alimentacao = form.save(commit=False)
        alimentacao.usuario = request.user
        alimentacao.save()
        messages.success(request, 'Alimentação registrada com sucesso!')
        return redirect('registrar_alimentacao')

    return render(request, 'form_base.html', {
        'form': form,
        'titulo': 'Registro de Alimentação',
    })

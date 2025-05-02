from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AlimentacaoForm

def registrar_alimentacao(request):
    form = AlimentacaoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Alimentação registrada com sucesso!')
        return redirect('registrar_alimentacao')

    return render(request, 'form_base.html', {
        'form': form,
        'titulo': 'Registro de Alimentação',
    })
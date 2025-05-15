from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import OrdenhaForm

@login_required
def registrar_ordenha(request):
    form = OrdenhaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        ordenha = form.save(commit=False)
        ordenha.usuario = request.user
        ordenha.save()
        messages.success(request, 'Ordenha registrada com sucesso!')
        return redirect('registrar_ordenha')

    return render(request, 'form_base.html', {
        'form': form,
        'titulo': 'Registro de Ordenha',
    })

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrdenhaForm

def registrar_ordenha(request):
    form = OrdenhaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Ordenha registrada com sucesso!')
        return redirect('registrar_ordenha')

    return render(request, 'form_base.html', {
        'form': form,
        'titulo': 'Registro de Ordenha',
    })

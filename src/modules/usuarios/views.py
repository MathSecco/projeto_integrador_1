from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PerfilForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Usuario ou senha inválidos.")
    else:
        form = AuthenticationForm()
    return render(request, "usuario/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")


def registro_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso!")
            return redirect("login")
        else:
            messages.error(request, "Erro ao criar a conta.")
    else:
        form = UserCreationForm()
    return render(request, "usuario/registro.html", {"form": form})


@login_required
def perfil_view(request):
    if request.method == "POST":
        form = PerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect("perfil")
        else:
            messages.error(request, "Erro ao atualizar o perfil.")
    else:
        form = PerfilForm(instance=request.user)
    return render(request, "usuario/perfil.html", {
        "form": form,
        "usuario": request.user
    })


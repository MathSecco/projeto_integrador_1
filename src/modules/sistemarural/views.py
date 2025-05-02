# sistemarural/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def teste(request):
    return render(request, 'teste.html')

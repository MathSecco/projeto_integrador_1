from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_alimentacao, name='registrar_alimentacao'),
]

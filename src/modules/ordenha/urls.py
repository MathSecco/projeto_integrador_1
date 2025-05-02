from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_ordenha, name='registrar_ordenha'),
]

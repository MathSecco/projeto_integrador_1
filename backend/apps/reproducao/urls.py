from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_reproducao, name='registrar_reproducao'),
]

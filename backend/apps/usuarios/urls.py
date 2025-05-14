from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('alterar-senha/', auth_views.PasswordChangeView.as_view(
    template_name='usuario/alterar_senha.html',
    success_url='/usuario/perfil/'
), name='alterar_senha'),
]

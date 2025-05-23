"""
URL configuration for sistemarural project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home, dashboard
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    
    
    path('ordenha/', include('apps.ordenha.urls')),
    path('alimentacao/', include('apps.alimentacao.urls')),
    path('saude/', include('apps.saude.urls')),
    path('reproducao/', include('apps.reproducao.urls')),

    path('usuario/', include('apps.usuarios.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
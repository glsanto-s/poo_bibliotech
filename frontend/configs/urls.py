"""
URL configuration for frontend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from app.views import listar_livros, categoria, logar, registrar, reservar, emprestar, atualizar_usuario, acoes, sair_login, dashboard, devolucao, multar

urlpatterns = [
    path('catalogo/', listar_livros, name='catalogo'),
    path('catalogo/<categoria>/', categoria, name='categoria'),
    path('' , logar, name='login'),
    path('cadastro/', registrar, name='cadastro'),
    path('perfil/', atualizar_usuario, name='perfil'),
    path('reservar/<idlivro>', reservar, name='reservar'),
    path('update/', atualizar_usuario, name='atualizar_usuario'),
    path('emprestimo/<idlivro>/<int:tipolivro>/', emprestar, name='emprestimo'),
    path('acoes/', acoes, name='acoes'),
    path('sair/', sair_login, name='sair'),
    path('dashboard/', dashboard, name='dashboard'),
    path('devolucao/<idemprestimo>/', devolucao, name='devolucao'),
    path('multar', multar, name='multar'),
]

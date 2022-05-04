"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from testeView.views import retornaRequest, exibeTabela, Inicio, Contato

from Pessoa.views import lista_tp_pessoa, lista_fornecedores, lista_clientes, lista_usuarios
from Pessoa.views import cadastra_tp_pessoa, cadastra_fornecedor, cadastra_cliente, cadastra_usuario
from Pessoa.views import altera_tp_pessoa, altera_fornecedor, altera_cliente, altera_usuario
from Pessoa.views import exclui_tp_pessoa, exclui_fornecedor, exclui_cliente, exclui_usuario

from Item.views import lista_categorias, lista_itens
from Item.views import cadastra_categoria, cadastra_item
from Item.views import altera_categoria, altera_item
from Item.views import exclui_categoria, exclui_item

from Local.views import lista_cidades, lista_estados
from Local.views import cadastra_cidade, cadastra_estado
from Local.views import altera_cidade, altera_estado
from Local.views import exclui_cidade, exclui_estado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__exemplo', retornaRequest),
    path('__tabela', exibeTabela),
    path('inicio', Inicio),
    path('contato', Contato),
    path('lista-tipos-pessoa', lista_tp_pessoa),
    path('cadastra-tp-pessoa', cadastra_tp_pessoa),
    path('altera-tp-pessoa', altera_tp_pessoa),
    path('exclui-tp-pessoa', exclui_tp_pessoa),
    path('lista-fornecedores', lista_fornecedores),
    path('cadastra-fornecedor', cadastra_fornecedor),
    path('altera-fornecedor', altera_fornecedor),
    path('exclui-fornecedor', exclui_fornecedor),
    path('lista-clientes', lista_clientes),
    path('cadastra-cliente', cadastra_cliente),
    path('altera-cliente', altera_cliente),
    path('exclui-cliente', exclui_cliente),
    path('lista-usuarios', lista_usuarios),
    path('cadastra-usuario', cadastra_usuario),
    path('altera-usuario', altera_usuario),
    path('exclui-usuario', exclui_usuario),
    path('lista-categorias', lista_categorias),
    path('cadastra-categoria', cadastra_categoria),
    path('altera-categoria', altera_categoria),
    path('exclui-categoria', exclui_categoria),
    path('lista-itens', lista_itens),
    path('cadastra-item', cadastra_item),
    path('altera-item', altera_item),
    path('exclui-item', exclui_item),
    path('lista-estados', lista_estados),
    path('cadastra-estado', cadastra_estado),
    path('altera-estado', altera_estado),
    path('exclui-estado', exclui_estado),
    path('lista-cidades', lista_cidades),
    path('cadastra-cidade', cadastra_cidade),
    path('altera-cidade', altera_cidade),
    path('exclui-cidade', exclui_cidade),
    path('', Inicio),
]

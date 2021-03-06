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
from django.urls import path, include
from ViewsProject.views import retornaRequest, exibeTabela, Inicio, Contato
from Aplicacao.views import getMenu
from .views import login

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
from Local.views import  busca_cidades



urlpatterns = [
    path('admin/', admin.site.urls),
    path('__exemplo', retornaRequest),
    path('__tabela', exibeTabela),
    path('inicio', Inicio, name='inicio'),
    path('contato', Contato, name='contato'),
    path('lista-tipos-pessoa', lista_tp_pessoa, name='lista-tipos-pessoa'),
    path('cadastra-tp-pessoa', cadastra_tp_pessoa, name='cadastra-tp-pessoa'),
    path('altera-tp-pessoa/<int:id>', altera_tp_pessoa),
    path('exclui-tp-pessoa/<int:id>', exclui_tp_pessoa),
    path('lista-fornecedores', lista_fornecedores, name='lista-fornecedores'),
    path('cadastra-fornecedor', cadastra_fornecedor, name='cadastra-fornecedor'),
    path('altera-fornecedor/<int:id>', altera_fornecedor),
    path('exclui-fornecedor/<int:id>', exclui_fornecedor),
    path('lista-clientes', lista_clientes, name='lista-clientes'),
    path('cadastra-cliente', cadastra_cliente, name='cadastra-cliente'),
    path('altera-cliente/<int:id>', altera_cliente),
    path('exclui-cliente/<int:id>', exclui_cliente),
    path('lista-usuarios', lista_usuarios, name='lista-usuarios'),
    path('cadastra-usuario', cadastra_usuario, name='cadastra-usuario'),
    path('altera-usuario/<int:id>', altera_usuario),
    path('exclui-usuario/<int:id>', exclui_usuario),
    path('lista-categorias', lista_categorias, name='lista-categorias'),
    path('cadastra-categoria', cadastra_categoria, name='cadastra-categoria'),
    path('altera-categoria/<int:id>', altera_categoria),
    path('exclui-categoria/<int:id>', exclui_categoria),
    path('lista-itens', lista_itens, name='lista-itens'),
    path('cadastra-item', cadastra_item, name='cadastra-item'),
    path('altera-item/<int:id>', altera_item),
    path('exclui-item/<int:id>', exclui_item),
    path('lista-estados', lista_estados, name='lista-estados'),
    path('cadastra-estado', cadastra_estado, name='cadastra-estado'),
    path('altera-estado/<int:id>', altera_estado),
    path('exclui-estado/<int:id>', exclui_estado),
    path('lista-cidades', lista_cidades, name='lista-cidades'),
    path('cadastra-cidade', cadastra_cidade, name='cadastra-cidade'),
    path('altera-cidade/<int:id>', altera_cidade),
    path('exclui-cidade/<int:id>', exclui_cidade),
    path('accounts/', include('django.contrib.auth.urls')),
    path('busca_cidades/<int:id>', busca_cidades),
    path('', Inicio, name='inicio'),
    path('getMenu/',getMenu),
]

handler404 = 'core.views.pagina_inexistente'
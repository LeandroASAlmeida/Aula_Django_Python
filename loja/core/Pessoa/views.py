from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormCliente,FormTpPessoa,FormUsuario,FormFornecedor
from .models import Cliente,Fornecedor,TpPessoa,Usuario

# Create your views here. 
def lista_tp_pessoa(request):
    tipoPessoa = TpPessoa.objects.all()
    total = tipoPessoa.count
    return render(request, 'lista_tp_pessoa.html',{'tipos':tipoPessoa , 'total': total })

def cadastra_tp_pessoa(request):
    return render(request, 'cadastra_tp_pessoa.html')

def altera_tp_pessoa(request):
    return render(request, 'altera_tp_pessoa.html')

def exclui_tp_pessoa(request):
    return render(request, 'exclui_tp_pessoa.html')

def lista_clientes(request):
    cliente = Cliente.objects.all()
    total = cliente.count
    return render(request, 'lista_clientes.html',{ 'cliente': cliente, 'total': total })

def cadastra_cliente(request):
    return render(request, 'cadastra_cliente.html')

def altera_cliente(request):
    return render(request, 'altera_cliente.html')

def exclui_cliente(request):
    return render(request, 'exclui_cliente.html')

def lista_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    total = fornecedores.count
    return render(request, 'lista_fornecedores.html',{'fornecedores': fornecedores, 'total': total})

def cadastra_fornecedor(request):
    return render(request, 'cadastra_fornecedor.html')

def altera_fornecedor(request):
    return render(request, 'altera_fornecedor.html')

def exclui_fornecedor(request):
    return render(request, 'exclui_fornecedor.html')

def lista_usuarios(request):
    usuario = Usuario.objects.all()
    total = usuario.count
    return render(request, 'lista_usuarios.html',{'usuario':usuario, 'total': total})

def cadastra_usuario(request):
    return render(request, 'cadastra_usuario.html')

def altera_usuario(request):
    return render(request, 'altera_usuario.html')

def exclui_usuario(request):
    return render(request, 'exclui_usuario.html')
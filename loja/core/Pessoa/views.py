from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

from .forms import FormTpPessoa, FormCliente, FormFornecedor, FormUsuario
from .models import TpPessoa, Cliente, Fornecedor, Usuario
from Local.models import Estado, Cidade
from ViewsProject.views import efetua_paginacao


# Create your views here.
def lista_tp_pessoa(request):
    procura = request.GET.get('procura')

    if procura:
        tipoPessoa = TpPessoa.objects.filter(descricao__icontains=procura)
    else:
        tipoPessoa = TpPessoa.objects.all()
        
    total = tipoPessoa.count

    dados = {
                'tipos' : tipoPessoa, 
                'total' : total, 
                'procura' : procura,
                'porPagina' : efetua_paginacao(request, tipoPessoa)
            }

    return render(request, 'lista_tp_pessoa.html', dados)

@login_required
def cadastra_tp_pessoa(request):
    if request.method == 'POST':
        form = FormTpPessoa(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_tp_pessoa)
    return render(request, 'cadastra_tp_pessoa.html')

@login_required
def altera_tp_pessoa(request,id):
    tipo = TpPessoa.objects.get(id=id)
    if request.method == 'POST':
        form = FormTpPessoa(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect(lista_tp_pessoa)
    return render(request, 'altera_tp_pessoa.html', {'tipo' : tipo})

@login_required
def exclui_tp_pessoa(request,id):
    tipo = TpPessoa.objects.get(id=id)
    if request.method == 'POST':
        tipo.delete()
        return redirect(lista_tp_pessoa)
    return render(request, 'exclui_tp_pessoa.html', {'tipo' : tipo})

def lista_clientes(request):
    procura = request.GET.get('procura')

    if procura:
        cliente = Cliente.objects.filter(nome__icontains=procura)|Cliente.objects.filter(email__icontains=procura)
    else:
        cliente = Cliente.objects.all()

    total = cliente.count

    dados = {
                'cliente' : cliente, 
                'total' : total, 
                'procura' : procura,
                'porPagina' : efetua_paginacao(request, cliente)
            }

    return render(request, 'lista_clientes.html', dados)

def cadastra_cliente(request):
    tp_pessoa = TpPessoa.objects.all()
    estados = Estado.objects.all()
    cidades = Cidade.objects.all()
    if request.method == 'POST':
        form = FormCliente(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_clientes)
    return render(request, 'cadastra_cliente.html', {'tipo' : tp_pessoa, 'cidades' : cidades,'estados' : estados})

def altera_cliente(request,id):
    cliente = Cliente.objects.get(id=id)
    tipo = TpPessoa.objects.all()
    estados = Estado.objects.all()
    cidades = Cidade.objects.all()
    tipoCliente = TpPessoa.objects.get(id=cliente.tp_pessoa_id)
    estadoCliente = Estado.objects.get(id=cliente.estado_id)
    cidadeCliente = Cidade.objects.get(id=cliente.cidade_id)
    dados = {
                'cliente' : cliente, 
                'tipos' : tipo, 
                'tipoPessoa' : tipoCliente.id,
                'estados' : estados,
                'cidades' : cidades,
                'estadoCliente' : estadoCliente.id,
                'cidadeCliente' : cidadeCliente.id
            }
    if request.method == 'POST':
        form = FormCliente(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect(lista_clientes)
    return render(request, 'altera_cliente.html', dados)

def exclui_cliente(request,id):
    cliente = Cliente.objects.get(id=id)
    tp_pessoa = TpPessoa.objects.get(id=cliente.tp_pessoa_id)
    estado = Estado.objects.get(id=cliente.estado_id)
    cidade = Cidade.objects.get(id=cliente.cidade_id)
    dados = {
            'cliente' : cliente, 
            'tp_pessoa' : tp_pessoa, 
            'estado' : estado,
            'cidade' : cidade
        }
    if request.method == 'POST':
        cliente.delete()
        return redirect(lista_clientes)

    return render(request, 'exclui_cliente.html', dados)

def lista_fornecedores(request):
    procura = request.GET.get('procura')

    if procura:
        fornecedores = Fornecedor.objects.filter(fantasia__icontains=procura)
    else:
        fornecedores = Fornecedor.objects.all()

    total = fornecedores.count

    dados = {
                'fornecedores' : fornecedores, 
                'total' : total, 
                'procura' : procura,
                'porPagina' : efetua_paginacao(request, fornecedores)
            }

    return render(request, 'lista_fornecedores.html', dados)

def cadastra_fornecedor(request):
    tp_pessoa = TpPessoa.objects.all()
    estados = Estado.objects.all()
    cidades = Cidade.objects.all()
   
    if request.method == 'POST':
        form = FormFornecedor(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_fornecedores)
    return render(request, 'cadastra_fornecedor.html', {'tipos' : tp_pessoa, 'estados' : estados, 'cidades' : cidades})

def altera_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    form = FormFornecedor(request.POST, instance=fornecedor)
    tp_pessoa = TpPessoa.objects.all()
    tipoFornecedor = TpPessoa.objects.get(id=fornecedor.tp_pessoa_id)
    estados = Estado.objects.all()
    cidades = Cidade.objects.all()
    estadoFornecedor = Estado.objects.get(id=fornecedor.estado_id)
    cidadeFornecedor = Cidade.objects.get(id=fornecedor.cidade_id)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista_fornecedores)
    
    dados = {
                'fornecedor' : fornecedor,
                'tipoPessoa' : tp_pessoa,
                'tipoFornecedor' : tipoFornecedor,
                'estados' : estados,
                'cidades' : cidades,
                'estadoFornecedor' : estadoFornecedor,
                'cidadeFornecedor' : cidadeFornecedor,
            }
    return render(request, 'altera_fornecedor.html', dados)

def exclui_fornecedor(request,id):
    fornecedor = Fornecedor.objects.get(id=id)
    tp_pessoa = TpPessoa.objects.get(id=fornecedor.tp_pessoa_id)
    estado = Estado.objects.get(id=fornecedor.estado_id)
    cidade = Cidade.objects.get(id=fornecedor.cidade_id)

    dados = {
                'fornecedor' : fornecedor,
                'tp_pessoa' : tp_pessoa,
                'estado' : estado,
                'cidade' : cidade
            }

    if request.method == 'POST':
        fornecedor.delete()
        return redirect(lista_fornecedores)
    return render(request, 'exclui_fornecedor.html', dados)

def lista_usuarios(request):


    procura= request.GET.get('procura')

    if procura:
        usuario = User.objects.filter(nome__icontains=procura)
    else:
        usuario = User.objects.all()

    total = usuario.count

    dados = {
                'usuarios' : usuario, 
                'total' : total, 
                'procura' : procura,
                'porPagina' : efetua_paginacao(request, usuario)
            }

    return render(request, 'lista_usuarios.html', dados)

def cadastra_usuario(request):
    if request.method == 'POST':
        try:
            validaUsuario = User.objects.get(username=request.POST['login'])

            if validaUsuario:
                return render(request,'cadastra_usuario.html', {'msg' : 'Usuário existente!'})
        except User.DoesNotExist:
            primeiroNome = request.POST['nome']
            segundoNome = request.POST['sobrenome']
            login = request.POST['login']
            senha = request.POST['senha']
        
            novoUsuario = User.objects.create_user(first_name=primeiroNome, last_name=segundoNome,username=login,password=senha)
            novoUsuario.save()
            return redirect(lista_usuarios)
    return render(request, 'cadastra_usuario.html')

def altera_usuario(request,id):
    usuario = User.objects.get(id=id)
    # form = FormUsuario(request.POST, instance=usuario)
    # if request.method == 'POST':
    #     if form.is_valid():
    #         form.save()
    #         return redirect(lista_usuarios)
    return render(request, 'altera_usuario.html',{'usuario' : usuario})

def exclui_usuario(request,id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect(lista_usuarios)
    return render(request, 'exclui_usuario.html', {'usuario' : usuario})
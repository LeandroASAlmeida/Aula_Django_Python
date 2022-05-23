from django.shortcuts import redirect, render

from .forms import FormTpPessoa, FormCliente, FormFornecedor, FormUsuario
from .models import TpPessoa, Cliente, Fornecedor, Usuario
from Local.models import Estado, Cidade


# Create your views here.
def lista_tp_pessoa(request):
    procura = request.GET.get('procura')

    if procura:
        tipoPessoa = TpPessoa.objects.filter(descricao__icontains=procura)
    else:
        tipoPessoa = TpPessoa.objects.all()
        
    total = tipoPessoa.count
    return render(request, 'lista_tp_pessoa.html', {'tipos' : tipoPessoa, 'total' : total, 'procura' : procura})

def cadastra_tp_pessoa(request):
    if request.method == 'POST':
        form = FormTpPessoa(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_tp_pessoa)
    return render(request, 'cadastra_tp_pessoa.html')

def altera_tp_pessoa(request,id):
    tipo = TpPessoa.objects.get(id=id)
    if request.method == 'POST':
        form = FormTpPessoa(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect(lista_tp_pessoa)
    return render(request, 'altera_tp_pessoa.html', {'tipo' : tipo})

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
    return render(request, 'lista_clientes.html', {'cliente' : cliente, 'total' : total, 'procura' : procura})

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
    dados = {
                'cliente' : cliente, 
                'tipos' : tipo, 
                'tipoPessoa' : tipoCliente.id,
                'estados' : estados,
                'cidades' : cidades,
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
    if request.method == 'POST':
        cliente.delete()
        return redirect(lista_clientes)
    return render(request, 'exclui_cliente.html', {'cliente' : cliente, 'tp_pessoa' : tp_pessoa})

def lista_fornecedores(request):
    procura = request.GET.get('procura')

    if procura:
        fornecedores = Fornecedor.objects.filter(fantasia__icontains=procura)
    else:
        fornecedores = Fornecedor.objects.all()

    total = fornecedores.count
    return render(request, 'lista_fornecedores.html', {'fornecedores' : fornecedores, 'total' : total, 'procura' : procura})

def cadastra_fornecedor(request):
    tp_pessoa = TpPessoa.objects.all()
    if request.method == 'POST':
        form = FormFornecedor(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_fornecedores)
    return render(request, 'cadastra_fornecedor.html', {'tipos' : tp_pessoa})

def altera_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    form = FormFornecedor(request.POST, instance=fornecedor)
    tp_pessoa = TpPessoa.objects.all()
    tipoFornecedor = TpPessoa.objects.get(id=fornecedor.tp_pessoa_id)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista_fornecedores)
    
    dados = {
                'fornecedor' : fornecedor,
                'tipoPessoa' : tp_pessoa,
                'tipoFornecedor' : tipoFornecedor
            }
    return render(request, 'altera_fornecedor.html', dados)

def exclui_fornecedor(request,id):
    fornecedor = Fornecedor.objects.get(id=id)
    tp_pessoa = TpPessoa.objects.get(id=fornecedor.tp_pessoa_id)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect(lista_fornecedores)
    return render(request, 'exclui_fornecedor.html', {'fornecedor' : fornecedor, 'tp_pessoa' : tp_pessoa})

def lista_usuarios(request):
    procura= request.GET.get('procura')

    if procura:
        usuario = Usuario.objects.filter(nome__icontains=procura)
    else:
        usuario = Usuario.objects.all()

    total = usuario.count
    return render(request, 'lista_usuarios.html', {'usuarios' : usuario, 'total' : total, 'procura' : procura})

def cadastra_usuario(request):
    if request.method == 'POST':
        form = FormUsuario(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_usuarios)
    return render(request, 'cadastra_usuario.html')

def altera_usuario(request,id):
    usuario = Usuario.objects.get(id=id)
    form = FormUsuario(request.POST, instance=usuario)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista_usuarios)
    return render(request, 'altera_usuario.html',{'usuario' : usuario})

def exclui_usuario(request,id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect(lista_usuarios)
    return render(request, 'exclui_usuario.html', {'usuario' : usuario})
from django.shortcuts import render, redirect
from .forms import FormCliente, FormFornecedor, FormTpPessoa, FormUsuario
from .models import Cliente, Fornecedor, TpPessoa, Usuario
from Local.models import  Estado, Cidade

# Create your views here.
def lista_tp_pessoas(request):
    procura = request.GET.get('procura')# get metodo e get função.

    if procura:
        tipoPessoa = TpPessoa.objects.filter(descricao__icontains=procura)|TpPessoa.objects.filter(id__icontains=procura)
    else:
        tipoPessoa=TpPessoa.objects.all()

    total = tipoPessoa.count
    return render(request,'lista_tp_pessoa.html',{ 'tipos' : tipoPessoa, 'total' : total, 'procura': procura })

def cadastra_tp_pessoa(request):
    if request.method == 'POST':
        form = FormTpPessoa(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_tp_pessoas)
    return render(request,'cadastra_tp_pessoa.html')

def altera_tp_pessoa(request,id):
    tipo = TpPessoa.objects.get(id=id)
    if request.method == 'POST':
        form = FormTpPessoa(request.POST,instance=tipo)
        if form.is_valid():
            form.save()
            return redirect(lista_tp_pessoas)
    return render(request,'altera_tp_pessoa.html',{ 'tipo' : tipo })

def exclui_tp_pessoa(request,id):
    tipo=TpPessoa.objects.get(id=id)

    if request.method == 'POST':
        tipo.delete()
        return redirect(lista_tp_pessoas)
    return render(request,'exclui_tp_pessoa.html',{ 'tipo': tipo })

def lista_clientes(request):
    procura = request.GET.get('procura')

    if procura:
        cliente = Cliente.objects.filter(nome__icontains=procura)|Cliente.objects.filter(email__icontains=procura)
    else:
        cliente = Cliente.objects.all()
    total = cliente.count
    return render(request,'lista_clientes.html',{ 'cliente' : cliente, 'total' : total,'procura':procura })

def cadastra_cliente(request):
    tp_pessoa = TpPessoa.objects.all()
    estados = Estado.objects.all()
    cidades = Estado.objects.all()
    if request.method == 'POST':
        form = FormCliente(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_clientes)
    return render(request,'cadastra_cliente.html',{'tipo' : tp_pessoa, 'cidades':cidades, 'estado':estados})

def altera_cliente(request,id):
    cliente = Cliente.objects.get(id=id)
    estados = Estado.objects.all()
    cidades = Estado.objects.all()
    tipo = TpPessoa.objects.all()
    tipoCliente = TpPessoa.objects.get(id=cliente.tp_pessoa_id)
    dados = { 
                'cliente' : cliente, 
                'tipos' : tipo, 
                'tipoPessoa' : tipoCliente.id ,
                'cidades':cidades,
                'estados':estados
            }
    if request.method == 'POST':
        form = FormCliente(request.POST,instance=cliente)
        if form.is_valid():
            form.save()
            return redirect(lista_clientes)
    return render(request,'altera_cliente.html',dados)

def exclui_cliente(request,id):
    cliente=Cliente.objects.get(id=id)
    estados = Estado.objects.all()
    cidades = Estado.objects.all()
    tipo= TpPessoa.objects.get(id=cliente.tp_pessoa_id)

    if request.method == 'POST':
        cliente.delete()
        return redirect(lista_clientes)
    return render(request,'exclui_cliente.html',{'cliente':cliente , 'tipo':tipo, 'cidades':cidades, 'estados':estados})

def lista_fornecedores(request):
    procura = request.GET.get('procura')

    if procura:
        fornecedores = Fornecedor.objects.filter(nome__icontains=procura)
    else:
        fornecedores = Fornecedor.objects.all()

    total = fornecedores.count
    return render(request,'lista_fornecedores.html',{ 'fornecedores' : fornecedores, 'total' : total,'procura':procura  })

def cadastra_fornecedor(request):
    tipo = TpPessoa.objects.all()
    estados = Estado.objects.all()
    cidades = Estado.objects.all()
    if request.method == 'POST':
        form = FormFornecedor(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_fornecedores)
    return render(request,'cadastra_fornecedor.html',{'tipos' : tipo,'cidades':cidades, 'estados':estados})

def altera_fornecedor(request,id):
    fornecedor = Fornecedor.objects.get(id = id)
    estados = Estado.objects.all()
    cidades = Estado.objects.all()
    form = FormFornecedor(request.POST, instance = fornecedor)
    tppessoa = TpPessoa.objects.all()
    tipoFornecedor = TpPessoa.objects.get(id = fornecedor.tp_pessoa_id)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista_fornecedores)

    dados={
        'fornecedor' : fornecedor,
        'tipoPessoa': tppessoa,
        'tipoFornecedor': tipoFornecedor,
        'cidades':cidades,
        'estados':estados

    }

    return render(request,'altera_fornecedor.html',dados)

def exclui_fornecedor(request,id):
    fornecedor = Fornecedor.objects.get(id=id)
    estados = Estado.objects.all()
    cidades = Estado.objects.all()
    tipo = TpPessoa.objects.get(id=fornecedor.tp_pessoa_id)

    if request.method == 'POST':
        fornecedor.delete()
        return redirect(lista_fornecedores)
    return render(request,'exclui_fornecedor.html',{'forn': fornecedor, 'tipo':tipo,'cidades':cidades,'estados':estados})

def lista_usuarios(request):
    procura = request.GET.get('procura')

    if procura:
        usuario = Usuario.objects.filter(nome__icontains=procura)| Usuario.objects.filter(sobrenome__icontains=procura)
    else:
        usuario = Usuario.objects.all()

    total = usuario.count
    return render(request,'lista_usuarios.html',{ 'usuarios' : usuario, 'total' : total,'procura':procura  })

def cadastra_usuario(request):
    if request.method == 'POST':
        form = FormUsuario(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_usuarios)
    return render(request,'cadastra_usuario.html')

def altera_usuario(request,id):
    usuario = Usuario.objects.get(id = id)
    form = FormUsuario(request.POST, instance = usuario)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista_usuarios)
    return render(request,'altera_usuario.html',{'usuario': usuario})

def exclui_usuario(request ,id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect(lista_usuarios)
    return render(request,'exclui_usuario.html',{'usuario': usuario})
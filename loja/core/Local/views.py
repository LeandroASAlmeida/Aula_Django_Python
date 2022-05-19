from django.shortcuts import render, redirect
from .forms import FormCidade, FormEstado
from. models import Estado, Cidade

# Create your views here.
def lista_estados(request):
    estado = Estado.objects.all()
    total = estado.count
    return render(request,'lista_estados.html',{'estado' : estado, 'total' : total })

def cadastra_estado(request):
    if request.method == 'POST':
        form = FormEstado(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_estados)
    return render(request,'cadastra_estado.html')

def altera_estado(request,id):
    estado= Estado.objects.get(id=id)
    form=FormEstado(request.POST, instance=estado)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista_estados)

    return render(request,'altera_estado.html',{'estado': estado})

def exclui_estado(request,id):
    estado= Estado.objects.get(id=id)

    if request.method == 'POST':
        estado.delete()
        return redirect(lista_estados)

    return render(request,'exclui_estado.html',{'estado':estado})

def lista_cidades(request):
    cidades = Cidade.objects.all()
    total = cidades.count
    return render(request,'lista_cidades.html', { 'cidades' : cidades, 'total' : total })

def cadastra_cidade(request):
    estado = Estado.objects.all()
    if request.method == 'POST':
        form = FormCidade(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_cidades)
    return render(request,'cadastra_cidade.html', { 'estados' : estado })

def altera_cidade(request,id): # dois parametros
    cidade= Cidade.objects.get(id=id)# chave primaria
    estados = Estado.objects.all()
    estadoId = Estado.objects.get(id=cidade.estado_id)
    form=FormCidade(request.POST,instance=cidade)
    dados = {

        'cidades': cidade,
        'estados': estados,  # SEMPRE PEDIR A CHAVE DO DICIONARIO
        'estadoId': estadoId.id
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()    #AQUI QUE FAZ AS ALTERAÇÕES
            return redirect(lista_cidades)
    return render(request,'altera_cidade.html',dados)

def exclui_cidade(request,id):# passar o id para excluir determinada cidade
    cidade = Cidade.objects.get(id=id)
    estado = Estado.objects.get(id=cidade.estado_id)

    if request.method == 'POST':
        cidade.delete()
        return redirect(lista_cidades)
    return render(request,'exclui_cidade.html',{'cidade':cidade, 'estado': estado})
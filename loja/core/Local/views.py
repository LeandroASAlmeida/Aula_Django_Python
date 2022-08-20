from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import FormEstado, FormCidade
from .models import Estado, Cidade
from ViewsProject.views import efetua_paginacao

# Create your views here.
def lista_estados(request):
    procura = request.GET.get('procura')

    if procura:
        estado = Estado.objects.filter(nome__icontains=procura)|Estado.objects.filter(sigla__icontains=procura)
    else:
        estado = Estado.objects.all()

    total = estado.count

    dados = {
                'estado' : estado, 
                'total' : total, 
                'procura' : procura,
                'porPagina' : efetua_paginacao(request, estado)
            }

    return render(request, 'lista_estados.html', dados)

def cadastra_estado(request):
    if request.method == 'POST':
        form = FormEstado(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_estados)
    return render(request, 'cadastra_estado.html')

def altera_estado(request,id):
    estado = Estado.objects.get(id=id)
    form = FormEstado(request.POST, instance=estado)
    if form.is_valid():
        form.save()
        return redirect(lista_estados)
    return render(request, 'altera_estado.html', {'estado' : estado})

def exclui_estado(request, id):
    estado = Estado.objects.get(id=id)
    if request.method == 'POST':
        estado.delete()
        return redirect(lista_estados)
    return render(request, 'exclui_estado.html', {'estado' : estado})

def lista_cidades(request):
    procura = request.GET.get('procura')

    if procura:
        cidades = Cidade.objects.filter(nome__icontains=procura)
    else:
        cidades = Cidade.objects.all()

    total = cidades.count

    dados = {
                'cidades' : cidades, 
                'total': total, 
                'procura' : procura,
                'porPagina' : efetua_paginacao(request, cidades)
            }

    return render(request, 'lista_cidades.html', dados)

def cadastra_cidade(request):
    estado = Estado.objects.all()
    if request.method == 'POST':
        form = FormCidade(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_cidades)
    return render(request, 'cadastra_cidade.html', {'estados' : estado})

def altera_cidade(request,id):
    cidade = Cidade.objects.get(id=id)
    estados = Estado.objects.all()
    estadoId = Estado.objects.get(id=cidade.estado_id)

    dados = {
                'cidade' : cidade,
                'estados' : estados,
                'estadoId' : estadoId
            }
    form = FormCidade(request.POST, instance=cidade)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista_cidades)
    return render(request, 'altera_cidade.html', dados)

def exclui_cidade(request, id):
    cidade = Cidade.objects.get(id=id)
    estado = Estado.objects.get(id=cidade.estado_id)
    if request.method == 'POST':
        cidade.delete()
        return redirect(lista_cidades)
    return render(request, 'exclui_cidade.html', {'cidade' : cidade, 'estado' : estado})

def busca_cidades(request, id):
    estado = Estado.objects.get(id=id)
    cidades = Cidade.objects.filter(estado_id=estado.id)

    dados = {}
    for cidade in cidades:
        dados[cidade.id] = cidade.nome

    return HttpResponse(str(dados))
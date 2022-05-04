from django.shortcuts import render

# Create your views here.
def lista_estados(request):
    return render(request, 'lista_estados.html')

def cadastra_estado(request):
    return render(request, 'cadastra_estado.html')

def altera_estado(request):
    return render(request, 'altera_estado.html')

def exclui_estado(request):
    return render(request, 'exclui_estado.html')

def lista_cidades(request):
    return render(request, 'lista_cidades.html')

def cadastra_cidade(request):
    return render(request, 'cadastra_cidade.html')

def altera_cidade(request):
    return render(request, 'altera_cidade.html')

def exclui_cidade(request):
    return render(request, 'exclui_cidade.html')
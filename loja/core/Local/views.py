from django.shortcuts import render

from .models import Cidade, Estado
from .forms import FormCidade,FormEstado

# Create your views here.
def lista_estados(request):
    estado = Estado.objects.all()
    total = estado.count
    return render(request, 'lista_estados.html',{'estado': estado,'total':total})

def cadastra_estado(request):
    return render(request, 'cadastra_estado.html')

def altera_estado(request):
    return render(request, 'altera_estado.html')

def exclui_estado(request):
    return render(request, 'exclui_estado.html')

def lista_cidades(request):
    cidade = Cidade.objects.all()
    total = cidade.count
    return render(request, 'lista_cidades.html',{'cidade': cidade,'total':total})

def cadastra_cidade(request):
    return render(request, 'cadastra_cidade.html')

def altera_cidade(request):
    return render(request, 'altera_cidade.html')

def exclui_cidade(request):
    return render(request, 'exclui_cidade.html')
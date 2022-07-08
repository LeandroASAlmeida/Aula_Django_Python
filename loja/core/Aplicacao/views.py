from django.http import HttpResponse
from django.shortcuts import render
from .models import Menu

# Create your views here.

def getMenu(request):
    menu = Menu.objects.all().order_by('descricao')
    itens ={}
    for item in menu:
        itens[item.descricao] = item.link
    return HttpResponse(str(itens))
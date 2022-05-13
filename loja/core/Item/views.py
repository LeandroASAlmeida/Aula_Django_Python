from django.shortcuts import render, redirect
from .forms import FormCategoria, FormItem
from .models import Categoria, Item

# Create your views here.
def lista_categorias(request):
    categorias = Categoria.objects.all()
    total = categorias.count
    return render(request,'lista_categorias.html',{ 'categorias' : categorias, 'total' : total })

def cadastra_categoria(request):
    if request.method == 'POST':
        form = FormCategoria(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_categorias)
    return render(request,'cadastra_categoria.html')

def altera_categoria(request,id):
    categoria = Categoria.objects.get(id=id)
    form = FormCategoria(request.POST, instance=categoria)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista_categorias)
    return render(request,'altera_categoria.html',{'categoria':categoria})

def exclui_categoria(request):
    return render(request,'exclui_categoria.html')

def lista_itens(request):
    item = Item.objects.all()
    total = item.count
    return render(request,'lista_itens.html',{ 'item' : item, 'total' : total })

def cadastra_item(request):
    categoria = Categoria.objects.all()
    if request.method == 'POST':
        form = FormItem(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_itens)
    return render(request,'cadastra_item.html',{ 'categorias' : categoria })

def altera_item(request,id):
    item = Item.objects.get(id=id)
    categorias = Categoria.objects.all()
    categoriaItem = Categoria.objects.get(id = item.categoria_id)
    form=FormItem(request.POST,instance=item)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista_itens)

    dados={
        'item': item,
        'categoriaItem': categoriaItem.id, 
        'categorias': categorias
        }
    return render(request,'altera_item.html', dados)

def exclui_item(request):
    return render(request,'exclui_item.html')
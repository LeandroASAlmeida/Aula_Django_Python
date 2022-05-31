from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def retornaRequest(self):
    msg = 'Hello world'
    return HttpResponse(msg)

def exibeTabela(self):
    tabela =    '<table border="1">'
    tabela+=        '<thead>'
    tabela+=            '<tr>' 
    tabela+=                '<th colpspan="2"> <font color="#FF0000">Cabeçalho</font> </th>' 
    tabela+=            '</tr>'
    tabela+=        '</thead>'
    tabela+=        '<tbody>'
    tabela+=            '<tr>' 
    tabela+=                '<td>Item 1</td><td>Item 2</td>' 
    tabela+=            '</tr>'
    tabela+=        '</tbody>'
    tabela+=        '<tfoot>'
    tabela+=            '<tr>' 
    tabela+=                '<td colpspan="2" bgcolor="#c3c3c3">&nbsp;</td>' 
    tabela+=            '</tr>'
    tabela+=        '</tfoot>'
    tabela+=    '</table>'
    return HttpResponse(tabela)

def Inicio(request):
    return render(request,'index.html')

def Contato(request):
    return render(request, 'contato.html')

def efetua_paginacao(request, registros):
    paginacao = Paginator(registros,5)

    try:
        pagina = int(request.GET.get('pagina','1'))
    except ValueError:
        pagina = 1

    try:
        registros = paginacao.page(pagina)
    except (PageNotAnInteger, EmptyPage):
        registros = paginacao.page(1)
    return registros
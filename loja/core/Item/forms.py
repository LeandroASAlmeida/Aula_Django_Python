from django import forms
from django.forms import ModelForm
from.models import Categoria,Item

class FormCategorias(ModelForm):
    class Meta: # Model Meta é basicamente a classe interna da sua classe de modelo.
        model = Categoria
        fields =['id','nome'] # colunas
        db_table = 'categoria'

class FormItem(ModelForm):
    class Meta: # Model Meta é basicamente a classe interna da sua classe de modelo.
        model = Item
        fields =['id','descricao','categoria']
        db_table = 'item'
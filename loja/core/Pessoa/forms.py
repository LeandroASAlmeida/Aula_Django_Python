from django.forms import ModelForm
from.models import TpPessoa,Cliente,Fornecedor,Usuario

class FormTpPessoa(ModelForm):
    class Meta: # Model Meta é basicamente a classe interna da sua classe de modelo.
        model = TpPessoa
        fields =['id','descricao'] # colunas
        db_table = 'TpPessoa'

class FormCliente(ModelForm):
    class Meta: # Model Meta é basicamente a classe interna da sua classe de modelo.
        model = Cliente
        fields =['id','nome','email','cpfcnpj','tp_pessoa'] 


class FormUsuario(ModelForm):
    class Meta: # Model Meta é basicamente a classe interna da sua classe de modelo.
        model = Usuario
        fields =['id','nome','sobrenome','login'] 
        db_table = 'usuario'

class FormFornecedor(ModelForm):
    class Meta: # Model Meta é basicamente a classe interna da sua classe de modelo.
        model = Fornecedor
        fields =['nome','fantasia','email','cpfcnpj','tp_pessoa']
        db_table = 'fornecedor'
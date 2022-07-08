from django.db import models

# Create your models here.
class Menu(models.Model):
    descricao = models.CharField(max_length=50 , blank=False, unique=True)
    link = models.CharField(max_length=50, blank=False, unique= True)

    class Meta:
        db_table = 'Menu'

    def __str__(self):
            return self.descricao

class Permissao(models.Model):
    id_usuario = models.IntegerField(blank=False)
    id_menu = models.ForeignKey(Menu,on_delete=models.PROTECT)
        
class Meta:
        db_table ='Permissoes'
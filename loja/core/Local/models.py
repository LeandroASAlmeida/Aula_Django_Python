from django.db import models

# Create your models here.

class Estado(models.Model):
    sigla = models.CharField(max_length=2, blank=False, unique=True)
    nome = models.CharField(max_length=50, blank=False, unique=True)

    class Meta:
        db_table = 'Estado'

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=50, blank=False, unique=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Cidade'

    def __str__(self):
        return self.nome
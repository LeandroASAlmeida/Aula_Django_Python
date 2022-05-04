from django.db import models

# Create your models here.
class CPFCNPJ(models.Model):
    numero = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.numero

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True)
    fone = models.CharField(max_length=11)
    cpf_cnpj = models.OneToOneField(CPFCNPJ, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'Cliente'
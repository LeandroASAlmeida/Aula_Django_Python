from django.contrib import admin
from .models import Cliente, CPFCNPJ

# Register your models here.

admin.site.register(CPFCNPJ)
admin.site.register(Cliente)
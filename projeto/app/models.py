from random import choices
from django.db import models
from django.forms import CharField

###############################################

class Rede(models.Model):
    nome_rede = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)

###############################################

class Pessoa(models.Model):

    ROLES = [
        (1,'ADMINISTRADOR'),
        (2, 'OPERADOR'),
        (3, 'GERENTE'),
    ] 
    nome = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    role = models.IntegerField(choices=ROLES)
    rede = models.ForeignKey("Rede", on_delete=models.DO_NOTHING)

###############################################

class Loja(models.Model):
    nome_loja = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    rede = models.ForeignKey("Rede", on_delete=models.DO_NOTHING)

###############################################

class Produto(models.Model):
    nome_produto = models.CharField(max_length=20)
    valor = models.DecimalField(decimal_places=2, max_digits=5)
    loja = models.ForeignKey("Loja", on_delete=models.DO_NOTHING)


###############################################

class ListaDeProdutos(models.Model):
    venda = models.ForeignKey("Venda", on_delete=models.DO_NOTHING)
    produto = models.ForeignKey("Produto", on_delete=models.DO_NOTHING)
    
###############################################

class Venda(models.Model):
    diaehora = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(decimal_places=2, max_digits=7,default=0.0)
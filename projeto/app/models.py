from django.db import models

###############################################

class Rede(models.Model):
    nome_rede = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    
    def __str__(self):
        return str(self.nome_rede)

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

    def __str__(self):
        return str(self.nome)


###############################################

class Loja(models.Model):
    nome_loja = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    rede = models.ForeignKey("Rede", on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.nome_loja)


###############################################

class Produto(models.Model):
    nome_produto = models.CharField(max_length=20)
    valor = models.DecimalField(decimal_places=2, max_digits=5)
    loja = models.ForeignKey("Loja", on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.nome_produto)

###############################################

class ListaDeProdutos(models.Model):
    venda = models.ForeignKey("Venda", on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField( default=1)
    produto = models.ForeignKey("Produto", on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return str(self.venda.id)

###############################################

class Venda(models.Model):
    diaehora = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(decimal_places=2, max_digits=7,default=0.0)
    
    def __str__(self):
        return str(self.id)

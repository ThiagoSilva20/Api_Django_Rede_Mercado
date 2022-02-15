from django.contrib import admin
from .models import Rede, Pessoa, Loja, Produto, ListaDeProdutos, Venda

admin.site.register(Rede)
admin.site.register(Pessoa)
admin.site.register(Loja)
admin.site.register(Produto)
admin.site.register(ListaDeProdutos)
admin.site.register(Venda)


#
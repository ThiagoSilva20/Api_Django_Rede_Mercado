from .models import Rede, Pessoa, Loja, Produto, ListaDeProdutos,Venda
from rest_framework import serializers

class RedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rede
        fields = ['id', 'nome_rede', 'cnpj']
class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'email', 'role', 'rede']
class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ['id','nome_loja', 'endereco', 'complemento', 'rede']
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome_produto', 'valor', 'loja']
class ListaDeProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaDeProdutos
        fields = ['id','venda','quantidade' , 'produto']
class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = ['id', 'total', 'diaehora',]
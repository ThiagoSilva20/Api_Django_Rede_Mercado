from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Rede, Pessoa, Loja, Produto, ListaDeProdutos, Venda
from .serializers import RedeSerializer, PessoaSerializer, LojaSerializer, ProdutoSerializer, ListaDeProdutosSerializer, VendaSerializer


########################################

from rest_framework import viewsets


########################################

class RedeView(viewsets.ModelViewSet):
    queryset = Rede.objects.all()
    serializer_class = RedeSerializer

########################################


class PessoaView(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

########################################

class LojaView(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer

########################################

class ProdutoView(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

########################################

class ListaDeProdutosView(viewsets.ModelViewSet):
    queryset = ListaDeProdutos.objects.all()
    serializer_class = ListaDeProdutosSerializer

########################################

class VendasView(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

######################################## 

@api_view(['GET'])
def busca_rede(request):
    str_busca = request.GET['rede']
    filtro = Rede.objects.filter(nome_rede__contains=str_busca)
    print(filtro)

    filtro2 = RedeSerializer(filtro, many=True).data
    return Response(data=filtro2)

########################################
@api_view(['GET'])
def busca_pessoa(request):
    str_busca = request.GET['pessoa']
    filtro = Pessoa.objects.filter(nome__contains=str_busca)
    print(filtro)

    filtro2 = PessoaSerializer(filtro, many=True).data
    return Response(data=filtro2)

########################################
@api_view(['GET'])
def busca_loja(request):
    str_busca = request.GET['loja']
    filtro = Loja.objects.filter(nome_loja__contains=str_busca)
    print(filtro)

    filtro2 = LojaSerializer(filtro, many=True).data
    return Response(data=filtro2)

########################################

@api_view(['GET'])
def busca_prod(request):
    str_busca = request.GET['produto']
    filtro = Produto.objects.filter(nome_produto__contains=str_busca)
    print(filtro)

    filtro2 = ProdutoSerializer(filtro, many=True).data
    return Response(data=filtro2)

########################################

@api_view(['GET'])
def busca_list(request):
    str_busca = request.GET['lista_de_produto']
    filtro = Produto.objects.filter(venda__contains=str_busca)
    print(filtro)

    filtro2 = ListaDeProdutosSerializer(filtro, many=True).data
    return Response(data=filtro2)

########################################

@api_view(['GET'])
def busca_venda(request):
    str_busca = request.GET['venda']
    filtro = Venda.objects.filter(total__contains=str_busca)
    print(filtro)

    filtro2 = VendaSerializer(filtro, many=True).data
    return Response(data=filtro2)
#########################################


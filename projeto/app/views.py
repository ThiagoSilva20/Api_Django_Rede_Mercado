from copy import error
from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Rede, Pessoa, Loja, Produto, ListaDeProdutos, Venda
from .serializers import RedeSerializer, PessoaSerializer, LojaSerializer, ProdutoSerializer, ListaDeProdutosSerializer, VendaSerializer


########################################

from rest_framework import viewsets



####################R####################

class RedeView(viewsets.ModelViewSet):
    queryset = Rede.objects.all()
    serializer_class = RedeSerializer

####################P####################


class PessoaView(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

####################L####################

class LojaView(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer

####################P####################

class ProdutoView(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

####################L####################

class ListaDeProdutosView(viewsets.ModelViewSet):
    queryset = ListaDeProdutos.objects.all()
    serializer_class = ListaDeProdutosSerializer

####################V####################

class VendasView(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

#####################V################### 

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

#########################################

@api_view(['GET'])
def busca_venda(request):
    str_busca = request.GET['venda']
    filtro = Venda.objects.filter(total__contains=str_busca)
    print(filtro)

    filtro2 = VendaSerializer(filtro, many=True).data
    return Response(data=filtro2)
#########################################

#venda
@api_view(['GET'])
def soma_precos(request, id):
    venda = Venda.objects.filter(id=id)
    list_produtos = ListaDeProdutos.objects.filter(venda=venda)
    total = 0
    for objeto in list_produtos:
        total += objeto.produto.valor * objeto.quantidade

    venda = list_produtos[0].venda
    venda.total = total
    venda.save()

    return Response(data=total)

############################################################################################################################################
    
@api_view(['GET'])
def fun_rede_g(request):
    rede = Rede.objects.all()
    serializer = RedeSerializer(rede, many=True)
    return Response(serializer.data)

##########################################

@api_view(['POST'])
def fun_rede_p(request):
    try:
        if not request.data.__contains__('nome_rede'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar nome da rede comércios."})
        
        if not request.data.__contains__('cnpj'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar cnpj da rede de comércios."})

        rede = Rede(nome_rede=request.data['nome_rede'], cnpj=request.data['cnpj'])
        rede.save()

        return Response(data=RedeSerializer(rede).data, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"messsage":"NÃO FOI POSSIVEL FAZER O POST"})

##########################################

@api_view(['DELETE'])
def fun_rede_d(request, id):
    try:
        dele = Rede.objects.get(pk=id)
        dele.delete()
        
    except Exception:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"messsage":"NÃO FOI POSSIVEL FAZER O PUT"} )

##########################################

@api_view(['PUT'])
def fun_rede_pu(request, id):


    try:
        if not request.data.__contains__('nome_rede'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar nome da rede comércios."})
        
        if not request.data.__contains__('cnpj'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar cnpj da rede de comércios."})

        rede = Rede.objects.get(pk=id)
        rede.nome_rede = request.data['nome_rede']
        rede.cnpj = request.data['cnpj']
        rede.save()

        return Response(data=RedeSerializer(rede).data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"messsage":"NÃO FOI POSSIVEL FAZER O PUT"})

##########################################

@api_view(['GET'])
def fun_rede_g1(request,id):
    try:
        rede = Rede.objects.get(pk=id)
        serializer = RedeSerializer(rede)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"messsage":"NÃO FOI POSSIVEL FAZER O PUT"})

############################################################################################################################################

@api_view(['GET'])
def fun_pessoa_g(request):
    pessoa = Pessoa.objects.all()
    serializer = PessoaSerializer(pessoa, many=True)
    return Response(serializer.data)

##########################################

@api_view(['POST'])
def fun_pessoa_p(request):
    try:
        if not request.data.__contains__('nome'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar nome."})
        
        if not request.data.__contains__('email'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar email."})
        
        if not request.data.__contains__('role'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar o trabalho."})
        
        if not request.data.__contains__('rede'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar a rede de comércio."})

        rede = Rede.objects.get(pk=request.data['rede'])

        pessoa = Pessoa(nome=request.data['nome'], email=request.data['email'], role=request.data['role'], rede=rede)
        pessoa.save()

        return Response(data=PessoaSerializer(pessoa).data, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"messsage":"NÃO FOI POSSIVEL FAZER O POST"})

##########################################

@api_view(['DELETE'])
def fun_pessoa_d(request, id):
    try:
        dele = Pessoa.objects.get(pk=id)
        dele.delete()
        return Response(status=status.HTTP_200_OK)
    except Exception:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"messsage":"NÃO FOI POSSIVEL FAZER O PUT"} )

##########################################

@api_view(['PUT'])
def fun_pessoa_pu(request, id):


    try:
        if not request.data.__contains__('nome'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar nome."})
        
        if not request.data.__contains__('email'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar email."})
        
        if not request.data.__contains__('role'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar o trabalho."})
        
        if not request.data.__contains__('rede'):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message":"Por favor informar a rede de comércio."})

        pessoa = Pessoa.objects.get(pk=id)
        pessoa.nome = request.data['nome']
        pessoa.email = request.data['email']
        pessoa.role = request.data['role']
        pessoa.rede = request.data['rede']
        pessoa.save()

        return Response(data=PessoaSerializer(pessoa).data, status=status.HTTP_200_OK)
    except Exception:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"messsage":"NÃO FOI POSSIVEL FAZER O PUT"})

##########################################

@api_view(['GET'])
def fun_pessoa_g1(request,id):
    try:
        pessoa = Pessoa.objects.get(pk=id)
        serializer = RedeSerializer(pessoa)
        return Response(serializer.data)
        
    except Exception:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"messsage":"NÃO FOI POSSIVEL PEGAR A INFORMAÇÃO"})

############################################################################################################################################

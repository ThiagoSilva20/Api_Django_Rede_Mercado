from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'Rede', views.RedeView)
router.register(r'Pessoa', views.PessoaView)
router.register(r'Loja', views.LojaView)
router.register(r'Produto', views.ProdutoView)
router.register(r'Lista_de_produtos', views.ListaDeProdutosView)
router.register(r'Venda', views.VendasView)

urlpatterns = [
    path('', include(router.urls)),
    path('search_rede', views.busca_rede),
    path('search_pessoa', views.busca_pessoa),
    path('search_loja', views.busca_loja),
    path('search_prod', views.busca_prod),
    path('search_list', views.busca_list),
    path('search_venda', views.busca_venda),
    ####
    path('calcula_venda/<int:id>', views.soma_precos),
    ####
    path('get_rede', views.fun_rede_g),
    path('post_rede', views.fun_rede_p),
    path('delete_rede/<int:id>', views.fun_rede_d),
    path('put_rede/<int:id>', views.fun_rede_pu),
    path('get_uni_rede/<int:id>', views.fun_rede_g1),
    ####
     path('get_pessoa', views.fun_pessoa_g),
     path('post_pessoa', views.fun_pessoa_p),
     path('delete_pessoa/<int:id>', views.fun_pessoa_d),
     path('put_pessoa/<int:id>', views.fun_pessoa_pu),
     path('get_uni_pessoa/<int:id>', views.fun_pessoa_g1),
     ####
     path('get_loja', views.fun_loja_g),
     path('post_loja', views.fun_loja_p),
     path('delete_loja/<int:id>', views.fun_loja_d),
     path('put_loja/<int:id>', views.fun_loja_pu),
     path('get_uni_loja/<int:id>', views.fun_loja_g1),
     ####
     path('get_produto', views.fun_produto_g),
     path('post_produto', views.fun_produto_p),
     path('delete_produto/<int:id>', views.fun_produto_d),
     path('put_produto/<int:id>', views.fun_produto_pu),
     path('get_uni_produto/<int:id>', views.fun_produto_g1),
     ####
     path('get_lista', views.fun_lista_g),
     path('post_lista', views.fun_lista_p),
     path('delete_lista/<int:id>', views.fun_lista_d),
     path('put_lista/<int:id>', views.fun_lista_pu),
     path('get_uni_lista/<int:id>', views.fun_lista_g1),
     ####
     path('get_venda', views.fun_venda_g),
     path('post_venda', views.fun_venda_p),
     path('delete_venda/<int:id>', views.fun_venda_d),
     path('put_venda/<int:id>', views.fun_venda_pu),
     path('get_uni_venda/<int:id>', views.fun_venda_g1),
     ####

]
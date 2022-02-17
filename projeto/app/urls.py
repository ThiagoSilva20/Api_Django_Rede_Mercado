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
    path('calcula_venda/<int:id>', views.soma_precos),
    path('get_rede', views.fun_rede_g),
    path('post_rede', views.fun_rede_p),
    path('delete_rede/<int:id>', views.fun_rede_d),
    path('put_rede/<int:id>', views.fun_rede_pu),
    path('get_uni_rede/<int:id>', views.fun_rede_g1),

]
from django.urls import path
from clientes.views.cliente_views import *
from clientes.views.pedido_views import *
from clientes.views.produto_views import *


urlpatterns = [
    path('listar', listar_clientes, name='listar_clientes'),
    path('cadastrar', inserir_cliente, name='cadastrar_cliente'),
    path('listar/<int:id>', listar_client_id, name='listar_cliente_id'),
    path('editar/<int:id>', editar_cliente, name='editar_cliente'),
    path('Remover/<int:id>', remover_cliente, name='remover_cliente'),
    path('cadastrar_pedido', inserir_pedido, name='cadastrar_pedido'),
    path('listar_pedidos', listar_pedidos, name='listar_pedidos'),
    path('listar_pedido/<int:id>', listar_pedido_id, name='listar_pedido_id'),
    path('editar_pedido/<int:id>', editar_pedido, name='editar_pedido'),
    path('cadastrar_produto', inserir_produto, name='cadastrar_produto'),
    path('lista_produtos', listar_produtos, name='lista_produtos'),
]

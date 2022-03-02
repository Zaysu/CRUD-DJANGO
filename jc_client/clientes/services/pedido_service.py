from ..models import Pedido
from .produto_service import *
from django.db import connection


def cadastrar_pedido(pedido):
    pedido_bd = Pedido.objects.create(cliente=pedido.cliente, data_pedido=pedido.data_pedido, valor=pedido.valor,
                                      status=pedido.status, observacoes=pedido.observacoes)
    pedido_bd.save()
    for i in pedido.produtos:
        produto = listar_produto_id(i.id)
        pedido_bd.produtos.add(produto)


def listar_pedido():
    # pedidos = Pedido.objects.all()
    # pedido = Pedido.objects.prefetch_related('produtos').all()
    pedidos = Pedido.objects.select_related('cliente').all()
    # for i in pedidos:
    # print(i.cliente.nome)
    # print(connection.queries)
    # print(len(connection.queries))
    return pedidos


def listar_pedido_id(id):
    endereco = Pedido.objects.get(id=id)
    return endereco


def editar_pedido(pedido_antigo, pedido_novo):
    pedido_antigo.cliente = pedido_novo.cliente
    pedido_antigo.data_pedido = pedido_novo.data_pedido
    pedido_antigo.valor = pedido_novo.valor
    pedido_antigo.status = pedido_novo.status
    pedido_antigo.observacoes = pedido_novo.observacoes
    pedido_antigo.produtos.set(pedido_novo.produtos)
    pedido_antigo.save(force_update=True)

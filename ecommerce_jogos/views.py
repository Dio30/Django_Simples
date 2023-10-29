from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from .models import ItensPedido, Pedidos, Jogos

@login_required()
def ver_lista(request):
    if request.user.is_authenticated:
        cliente = request.user
        pedido, criado = Pedidos.objects.get_or_create(cliente=cliente, complete=False)
        item_carrinho = pedido.pegar_carrinho_itens
    else:
        pedido = {'pegar_carrinho_total':0, 'pegar_carrinho_itens':0}
        item_carrinho = pedido['pegar_carrinho_itens']
    
    jogos = Jogos.objects.all()
    context = {
        'item_carrinho': item_carrinho,
        'jogos': jogos,
    }
    return render(request, 'home.html', context)

@login_required()
def cart(request):
    if request.user.is_authenticated:
        cliente = request.user
        pedido, criado = Pedidos.objects.get_or_create(cliente=cliente, complete=False)
        item_carrinho = pedido.pegar_carrinho_itens
        itens = pedido.itenspedido_set.all()
        
    else:
        itens = []
        pedido = {'pegar_carrinho_total':0, 'pegar_carrinho_itens':0, 'itens': itens}
        item_carrinho = pedido['pegar_carrinho_itens']
    
    context = {
        'item_carrinho': item_carrinho,
        'itens': itens,
        'pedido':pedido,
    }
    return render(request, "compras/cart.html", context)

def update_cart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('produtoId:',productId)
    print('action:',action)
    if request.user.is_authenticated:
        cliente = request.user
        jogo = Jogos.objects.get(id=productId)
        pedido, criado = Pedidos.objects.get_or_create(cliente=cliente, complete=False)
        itenspedido, criado = ItensPedido.objects.get_or_create(pedido=pedido, jogo=jogo, cliente=cliente)
    
    if action == 'add':
        itenspedido.quantidade = (itenspedido.quantidade + 1)
        
    elif action == 'remove':
        itenspedido.quantidade = (itenspedido.quantidade - 1)
        
    itenspedido.save()
    
    if itenspedido.quantidade <= 0:
        itenspedido.delete()
        
    return JsonResponse("Jogo adicionado com sucesso", safe=False)
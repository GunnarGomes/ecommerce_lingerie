from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Carrinho, ItemCarrinho
from produtos.models import Produto

@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id, disponivel=True)
    carrinho, criado = Carrinho.objects.get_or_create(usuario=request.user, finalizado=False)
    
    item_carrinho, criado_item = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
    
    if not criado_item:
        item_carrinho.quantidade += 1
        item_carrinho.save()
    
    messages.success(request, f'Produto "{produto.nome}" adicionado ao carrinho.')
    return redirect('produtos:detalhes_produto', slug=produto.slug)
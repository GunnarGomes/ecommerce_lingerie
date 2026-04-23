from django.shortcuts import get_object_or_404, redirect, render
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

@login_required
def ver_carrinho(request):
    carrinho = Carrinho.objects.filter(usuario=request.user, finalizado=False).first()

    if not carrinho:
        carrinho = Carrinho.objects.create(usuario=request.user, finalizado=False)
    itens = carrinho.itens.all()  # related_name='itens'
    total = sum(item.preco_total for item in itens)
    
    contexto = {
        'carrinho': carrinho,
        'itens': itens,
        'total': total,
    }
    return render(request, 'carrinho/ver_carrinho.html', contexto)

@login_required
def remover_do_carrinho(request, item_id):
    item_carrinho = get_object_or_404(ItemCarrinho, id=item_id, carrinho__usuario=request.user, carrinho__finalizado=False)
    item_carrinho.delete()
    messages.success(request, f'Produto "{item_carrinho.produto.nome}" removido do carrinho.')
    return redirect('carrinho:ver_carrinho')

@login_required
def atualizar_quantidade(request, item_id):
    item_carrinho = get_object_or_404(ItemCarrinho, id=item_id, carrinho__usuario=request.user, carrinho__finalizado=False)
    
    if request.method == 'POST':
        nova_quantidade = int(request.POST.get('quantidade', 1))
        if nova_quantidade > 0:
            item_carrinho.quantidade = nova_quantidade
            item_carrinho.save()
            messages.success(request, f'Quantidade do produto "{item_carrinho.produto.nome}" atualizada para {nova_quantidade}.')
        else:
            item_carrinho.delete()
            messages.success(request, f'Produto "{item_carrinho.produto.nome}" removido do carrinho.')
    
    return redirect('carrinho:ver_carrinho')

@login_required
def finalizar_carrinho(request):
    carrinho = Carrinho.objects.filter(usuario=request.user, finalizado=False).first()
    
    if not carrinho:
        messages.error(request, 'Não há carrinho para finalizar.')
        return redirect('produtos:lista_produtos')
    
    carrinho.finalizado = True
    carrinho.save()
    
    messages.success(request, 'Carrinho finalizado com sucesso! Obrigado pela sua compra.')
    return redirect('produtos:lista_produtos')
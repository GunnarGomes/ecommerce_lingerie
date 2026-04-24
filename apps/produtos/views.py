from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Categoria
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from carrinho.models import Carrinho, ItemCarrinho
from django.contrib import messages

def lista_produtos(request, categoria_slug=None):
    categoria = None
    categorias = Categoria.objects.all()
    produtos = Produto.objects.filter(disponivel=True)

    if categoria_slug:
        categoria = get_object_or_404(Categoria, slug=categoria_slug)
        produtos = produtos.filter(categoria=categoria)

    paginator = Paginator(produtos, 10)  # Exibe 10 produtos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'produtos/lista_produtos.html', {
        'categoria': categoria,
        'categorias': categorias,
        'produtos': page_obj,
    })

def detalhe_produto(request, produto_slug):
    produto = get_object_or_404(Produto, slug=produto_slug, disponivel=True)
    return render(request, 'produtos/detalhe_produto.html', {'produto': produto})



@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id, disponivel=True)
    
    # Busca ou cria o carrinho ativo do usuário
    carrinho, criado = Carrinho.objects.get_or_create(usuario=request.user, finalizado=False)
    
    # Busca ou cria o item no carrinho
    item_carrinho, criado_item = ItemCarrinho.objects.get_or_create(
        carrinho=carrinho, 
        produto=produto
    )
    
    # Se o item já existia, incrementa a quantidade
    if not criado_item:
        item_carrinho.quantidade += 1
        item_carrinho.save()
        messages.success(request, f'Quantidade do produto "{produto.nome}" foi aumentada!')
    else:
        # Item acabou de ser criado
        messages.success(request, f'Produto "{produto.nome}" adicionado ao carrinho!')
    
    # Sempre redirecionar para a mesma página (detalhe do produto) é uma boa experiência
    return redirect('produtos:detalhe_produto', slug=produto.slug)
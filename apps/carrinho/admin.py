from django.contrib import admin
from .models import Carrinho, ItemCarrinho

class ItemCarrinhoInline(admin.TabularInline):
    model = ItemCarrinho
    extra = 1
    fields = ('produto', 'quantidade', 'preco_unitario')

@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'criado_em', 'atualizado_em', 'finalizado')
    list_filter = ('finalizado', 'criado_em', 'atualizado_em')
    inlines = [ItemCarrinhoInline]

@admin.register(ItemCarrinho)
class ItemCarrinhoAdmin(admin.ModelAdmin):
    list_display = ('carrinho', 'produto', 'quantidade', 'preco_unitario', 'preco_total')
    search_fields = ('produto__finalizado',)


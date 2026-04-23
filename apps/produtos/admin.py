from django.contrib import admin
from .models import Categoria, Produto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'estoque', 'disponivel')
    list_filter = ('disponivel', 'categoria')
    search_fields = ('nome', 'descricao')
    prepopulated_fields = {'slug': ('nome',)}
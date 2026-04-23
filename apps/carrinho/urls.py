from django.urls import path
from . import views

app_name = 'carrinho'

urlpatterns = [
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar'),
    path('ver/', views.ver_carrinho, name='ver_carrinho'),
    path('remover/<int:item_id>/', views.remover_do_carrinho, name='remover'),
    path('atualizar/<int:item_id>/', views.atualizar_quantidade, name='atualizar'),
    path('limpar/', views.limpar_carrinho, name='limpar'),
    path('finalizar/', views.finalizar_carrinho, name='finalizar'),
]
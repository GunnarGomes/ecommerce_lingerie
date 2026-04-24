from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('categoria/<slug:slug>/', views.lista_produtos, name='produtos_por_categoria'),
    path('produto/<slug:slug>/', views.detalhe_produto, name='detalhe_produto'),
    path('busca/', views.busca_produtos, name='busca_produtos'),
]
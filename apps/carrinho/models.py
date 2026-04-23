from django.db import models

# Create your models here.
class Carrinho(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    finalizado = models.BooleanField(default=False)

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey('produtos.Produto', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.ForeignKey('produtos.Produto', on_delete=models.CASCADE, related_name='preco_unitario')
    

    @property
    def preco_total(self):
        return self.quantidade * self.preco_unitario
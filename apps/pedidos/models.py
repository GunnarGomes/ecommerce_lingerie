from django.db import models


class Pedido(models.Model):
    nome_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    endereco_entrega = models.CharField(max_length=255)
    data_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Pedido #{self.id} - {self.nome_cliente}'
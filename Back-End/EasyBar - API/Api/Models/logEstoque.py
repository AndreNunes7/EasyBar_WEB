from django.db import models
from .produtos import Produto

class MovimentacaoEstoque(models.Model):
    TIPOS_MOVIMENTACAO = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    tipo_movimentacao = models.CharField(max_length=50, choices=TIPOS_MOVIMENTACAO)
    data_movimentacao = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_movimentacao} de {self.quantidade} para {self.produto.nome} em {self.data_movimentacao}"

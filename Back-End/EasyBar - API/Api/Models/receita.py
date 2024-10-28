from django.db import models
from .produtos import Produto

class Receita(models.Model):
    id = models.AutoField(primary_key=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="receitas")
    quantidade = models.PositiveIntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    descricao = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Receita do produto: {self.produto.nome}, valor: {self.valor_total} - {self.data}"

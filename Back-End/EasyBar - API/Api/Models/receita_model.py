from django.db import models
from .produto_model import Produto
from .basic_model import Base

class Receita(Base):
    id = models.AutoField(primary_key=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    descricao = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Receita do produto: {self.produto}, tem o valor: {self.valor_total} - {self.data}"

from django.db import models
from .basic_model import Base

class Produto(Base):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    categoria = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - R${self.preco} - {self.estoque} unidades em estoque"

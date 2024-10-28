from django.db import models
from .fornecedores import Fornecedor

class Produto(models.Model):
    CATEGORIAS = [
        ('bebida', 'Bebida'),
        ('comida', 'Comida'),
        ('insumo', 'Insumo'),
        ('outros', 'Outros'),
    ]

    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.PositiveIntegerField()
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=True)
    data_validade = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.categoria}"

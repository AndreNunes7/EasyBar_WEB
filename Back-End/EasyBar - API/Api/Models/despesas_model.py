from django.db import models
from .basic_model import Base

class Despesa(Base):
    nome = models.CharField(max_length=80)
    descricao = models.TextField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    categoria = models.CharField(max_length=100, choices=[
        ('carnes', 'Carnes'),
        ('mercado', 'Mercado'),
        ('fornecedorX', 'FornecedorX'),
        ('fornecedorY', 'FornecedorY')
    ])  

    def __str__(self) -> str:
        return f"Despesas: {self.descricao} - Valor: {self.valor}"

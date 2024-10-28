from django.db import models
from .fornecedores import Fornecedor
from .produtos import Produto 

class Pagamento(models.Model):
    METODOS_PAGAMENTO = [
        ('dinheiro', 'Dinheiro'),
        ('cartao_credito', 'Cartão de Crédito'),
        ('cartao_debito', 'Cartão de Débito'),
        ('pix', 'Pix')
    ]

    id = models.AutoField(primary_key=True)
    fornecedor = models.ForeignKey(
        Fornecedor,
        on_delete=models.CASCADE,
        related_name="pagamentos"
    )
    produto = models.ForeignKey(
        Produto,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="pagamentos"
    )
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pagamento = models.CharField(max_length=50, choices=METODOS_PAGAMENTO)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Pagamento ao Fornecedor {self.fornecedor.nome}: valor {self.valor_pago} via {self.get_metodo_pagamento_display()}'

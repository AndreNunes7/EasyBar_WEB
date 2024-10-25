from django.db import models
from .basic_model import Base
from Api.Models.fornecedor_model import Fornecedor 

"""
    Model generica pode ser para pagamento de fornecedores ou outros 
    
    Exemplo - Empresas, funcionarios etc...
"""




"""
    Model para pagamento a fornecedores
"""

class PagamentoFornecedor(Base):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField(max_length=255, blank=True, null=True)
    fornecedor = models.ForeignKey(
        Fornecedor,
        on_delete=models.CASCADE,
        related_name="pagamentos",
    )
    metodo_pagamento = models.CharField(
        max_length=50,
        choices=[
            ('dinheiro', 'Dinheiro'),
            ('cartao_credito', 'Cartão de Crédito'),
            ('cartao_debito', 'Cartão de Débito'),
            ('transferencia', 'Transferência Bancária'),
            ('pix', 'Pix')
        ],
    )
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    numero_documento = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return f'Pagamento ao Fornecedor {self.fornecedor.nome}: valor {self.valor_pago}'

    class Meta:
        verbose_name = "Pagamento ao Fornecedor"
        verbose_name_plural = "Pagamentos aos Fornecedores"

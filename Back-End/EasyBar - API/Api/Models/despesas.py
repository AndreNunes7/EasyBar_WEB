from django.db import models

class Despesa(models.Model):
    CATEGORIAS = [
        ('folha_pagamento', 'Folha de Pagamento'),
        ('mercado', 'Mercado'),
        ('urgencias', 'Urgências'),
        ('contas', 'Contas'),
    ]

    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return f"{self.categoria} - {self.valor} em {self.data}"

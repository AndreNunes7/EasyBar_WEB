from django.db import models

class Relatorio(models.Model):
    TIPOS_RELATORIO = [
        ('vendas', 'Vendas'),
        ('financeiro', 'Financeiro'),
        ('estoque', 'Estoque'),
    ]

    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50, choices=TIPOS_RELATORIO)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    conteudo = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Relatório de {self.get_tipo_display()} ({self.data_inicio} a {self.data_fim})"

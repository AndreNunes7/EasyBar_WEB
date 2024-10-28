from datetime import date
from django.db import models
from django.db.models import Sum
from datetime import date

from .financeiro import Financeiro
from .despesas import Despesa
from .produtos import Produto



class Dashboard(models.Model):
    data = models.DateField(auto_now_add=True)

    @property
    def receita_mensal(self):
        inicio_mes = date.today().replace(day=1)
        return Financeiro.objects.filter(data__gte=inicio_mes).aggregate(Sum('total_receita'))['total_receita__sum'] or 0

    @property
    def despesa_mensal(self):
        inicio_mes = date.today().replace(day=1)
        return Despesa.objects.filter(data__gte=inicio_mes).aggregate(Sum('valor'))['valor__sum'] or 0

    @property
    def estoque_total(self):
        return Produto.objects.aggregate(Sum('quantidade_estoque'))['quantidade_estoque__sum'] or 0

    def __str__(self):
        return f"Dashboard - {self.data}"

from django.db import models

class Financeiro(models.Model):
    total_lucro = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_despesas = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    data = models.DateField(auto_now_add=True)
    lucro = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.lucro = self.total_lucro - self.total_despesas
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Financeiro - {self.data} (Lucro: {self.lucro})"

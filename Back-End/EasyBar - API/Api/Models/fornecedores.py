from django.db import models

class Fornecedor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, unique=True)
    documento = models.CharField(max_length=20, unique=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.nome} - {self.telefone}'

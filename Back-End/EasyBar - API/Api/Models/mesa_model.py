from django.db import models
from .basic_model import Base

class Mesa(Base):
    numero = models.CharField(max_length=50, unique=True)
    capacidade = models.PositiveIntegerField()
    status = models.CharField(max_length=50, choices=[
        ('disponivel', "Disponível"),
        ('reservada', "Reservada"),
        ('ocupada', "Ocupada"),
        ('cancelada', "Cancelada"),
    ])

    def __str__(self) -> str:
        return f"Mesa {self.numero} - Status: {self.status}"

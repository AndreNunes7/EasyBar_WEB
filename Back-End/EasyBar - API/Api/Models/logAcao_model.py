# logacao_model.py
from django.db import models
from .usuarios_model import Usuarios
from .basic_model import Base

class LogAcao(Base):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    acao = models.CharField(max_length=200)
    data_acao = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.usuario.username} - {self.acao} - {self.data_acao}'

    class Meta:
        verbose_name = 'Log de Ação'
        verbose_name_plural = 'Logs de Ações'

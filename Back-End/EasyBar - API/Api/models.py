from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    
    
    
class Usuarios(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups',  
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions',  
        related_query_name='custom_user'
    )
    
    cargo = models.CharField(max_length=80, choices=[
        ('admin', 'Administrador'),
        ('gerente', 'Gerente'),
        ('funcionario', 'Funcionário'),
    ])

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.username


    
class Produto(Base):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    categoria = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - R${self.preco} - {self.estoque} unidades em estoque"


    
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
    
class Receita(Base):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    descricao = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"Receita do produto: {self.produto}, tem o valor: {self.valor_total} - {self.data} "



class Comanda(Base):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    aberta = models.BooleanField(default=True)
    produtos = models.ManyToManyField(Produto, through='ComandaItem')
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self) -> str:
        return f"Comanda da mesa {self.mesa} - Status: {"Aberta" if self.aberta else "Fechada"}, valor total da comanda: {self.valor_total}"    

    
    
class ComandaItem(Base):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return f"Item {self.produto.nome} - Qtd: {self.quantidade}"
        
    
    
    
class Despesa(Base):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    categoria = models.CharField(max_length=100) # Ex aluguell
    
    
    def __str__(self) -> str:
        return f"Despesas: {self.descricao} - Valor: {self.valor}"
    
    

class Pagamento(Base):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    metodo_pagamento = models.CharField(max_length=50, choices=[
        ('dinheiro', 'Dinheiro'),
        ('cartao_credito', 'Cartão de Crédito'),
        ('cartao_debito', 'Cartão de Débito'),
        ('qr_code', 'QR Code'),
        ('pix', 'Pix')
    ])
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField()
    
    def __str__(self) -> str:
        return f'Pagamento da comanda: {self.comanda} - valor: {self.valor_pago}'
    
    
    
    
class LogAcao(Base):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)  
    acao = models.CharField(max_length=200)
    data_acao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.usuario.username} - {self.acao} - {self.data_acao}'  #
    
    class Meta:
        verbose_name = 'Log de Ação'
        verbose_name_plural = 'Logs de Ações'
    
    
    


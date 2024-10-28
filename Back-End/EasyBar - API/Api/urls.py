from django.contrib import admin
from django.urls import path, include
from .Views import *

urlpatterns = [
    
    # Users CRUD:
    path('users/', usuarios.get_users_all, name='listar_usuarios',),
    path('users/add/', usuarios.post_user, name='inserir_usuario'),
    
    # Produtos CRUD:
    path('produtos/', produtos.get_produtos_all, name='listar_produtos'),  
    path('produtos/add/', produtos.post_produtos, name='inserir_produto'),
    
    # Despesas CRUD:
    path('despesas/', despesas.get_despesas_all, name='listar_despesas'),
    path('despesas/add/', despesas.post_despesa, name='inserir_despesa'),
    
    # Receitas CRUD:
    path('receitas/', receitas.get_receitas_all, name='listar_receitas'),
    path('receitas/add/', receitas.post_receitas, name='inserir_receita'),
    
    # pagamentos CRUD:
    path('pagamentos/', pagamentos.get_pagamentos_fornecedores_all, name='listar_pagamentos'),
    path('pagamentos/add/', pagamentos.post_pagamentos, name='inserir_pagamento'),
    
    # Fornecedores CRUD:
    path('fornecedores/', fornecedores.get_fornecedores_all, name='listar_fornecedores'),
    path('fornecedores/add/', fornecedores.post_fornecedor, name='inserir_fornecedor'),
    
    # Financeiro CRUD:
    path('financeiro/', financeiro.get_financas_all, name='listar_financeiro'),
    path('financeiro/add/', financeiro.post_financas, name='inserir_financeiro'),
    
    # Relatorios CRUD:
    path('relatorios/', relatorio.get_relatorio_all, name='listar_relatorios'),
    path('relatorios/add/', relatorio.post_relatorio, name='inserir_relatorio'),
    
    # Dashboard CRUD:
    path('dashboard/', dashboard.get_dashboard, name='listar_dashboard'),
    path('dashboard/add/', dashboard.post_dashboard, name='inserir_dashboard'),
    
    # Log de Estoque:
    path('log_estoque/', logEstoque.get_movimentoEstoque_all, name='listar_log_estoque'),
    
]


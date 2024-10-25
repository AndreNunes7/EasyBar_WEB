from django.contrib import admin
from django.urls import path, include
from .Views import *

urlpatterns = [
    
    # Users CRUD:
    path('users/', usuarios_views.get_users_all, name='listar_usuarios',),
    path('users/add/', usuarios_views.post_user, name='inserir_usuario'),
    
    # Produtos CRUD:
    path('produtos/', produtos_views.get_produtos_all, name='listar_produtos'),  
    path('produtos/add/', produtos_views.post_produtos, name='inserir_produto'),
    
    # Despesas CRUD:
    path('despesas/', despesas_views.get_despesas_all, name='listar_despesas'),
    path('despesas/add/', despesas_views.post_despesa, name='inserir_despesa'),
    
    # Receitas CRUD:
    path('receitas/', receitas_views.get_receitas_all, name='listar_receitas'),
    path('receitas/add/', receitas_views.post_receitas, name='inserir_receita'),
    
    # pagamentos CRUD:
    path('pagamentos/', pagamentos_views.get_pagamentos_fornecedores_all, name='listar_pagamentos'),
    path('pagamentos/add/', pagamentos_views.post_pagamentos, name='inserir_pagamento'),
    
    # Mesas CRUD:
    path('mesas/', mesas_views.get_mesas_all, name='listar_mesas'),
    path('mesas/add/', mesas_views.post_mesa, name='inserir_mesa'),
    
    
]


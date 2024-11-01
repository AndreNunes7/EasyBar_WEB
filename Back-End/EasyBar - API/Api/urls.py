from django.urls import path, include
from .Views import *

urlpatterns = [
    
    # Login:
    
    
   
    
    # Produtos CRUD:
    path('produtos/', produtos.get_produtos_all, name='listar_produtos'),  
    path('produtos/add/', produtos.post_produtos, name='inserir_produto'),
    path('produtos/update/<int:id>/', produtos.update_produto, name='atualizar_produto'),
    path('produtos/delete/<int:id>/', produtos.delete_produto, name='deletar_produto'),
    
    # Despesas CRUD:
    path('despesas/', despesas.get_despesas_all, name='listar_despesas'),
    path('despesas/add/', despesas.post_despesa, name='inserir_despesa'),
    path('despesas/update/<int:id>/', despesas.update_despesa, name='atualizar_despesa'),
    path('despesas/delete/<int:id>/', despesas.delete_despesa, name='deletar_despesa'),
    
    # Receitas CRUD:
    path('receitas/', receitas.get_receitas_all, name='listar_receitas'),
    path('receitas/add/', receitas.post_receitas, name='inserir_receita'),
    path('receitas/update/<int:id>/', receitas.update_receitas, name='atualizar_receita'),
    path('receitas/delete/<int:id>/', receitas.delete_receitas, name='deletar_receita'),
    
    # pagamentos CRUD:
    path('pagamentos/', pagamentos.get_pagamentos_fornecedores_all, name='listar_pagamentos'),
    path('pagamentos/add/', pagamentos.post_pagamentos, name='inserir_pagamento'),
    path('pagamentos/update/<int:id>/', pagamentos.update_pagamento, name='atualizar_pagamento'),
    path('pagamentos/delete/<int:id>/', pagamentos.delete_pagamento, name='deletar_pagamento'),
    
    
    # Fornecedores CRUD:
    path('fornecedores/', fornecedores.get_fornecedores_all, name='listar_fornecedores'),
    path('fornecedores/add/', fornecedores.post_fornecedor, name='inserir_fornecedor'),
    path('fornecedores/update/<int:id>/', fornecedores.update_fornecedor, name='atualizar_fornecedor'),
    path('fornecedores/delete/<int:id>/', fornecedores.delete_fornecedor, name='deletar_fornecedor'),
    
    
    # Financeiro CRUD:
    path('financeiro/', financeiro.get_financas_all, name='listar_financeiro'),
    path('financeiro/add/', financeiro.post_financas, name='inserir_financeiro'),
    path('financeiro/update/<int:id>/', financeiro.update_financa, name='atualizar_finanças'),
    path('financeiro/delete/<int:id>/', financeiro.delete_financa, name='deletar_financeiro'),
    
    # Relatorios CRUD:
    path('relatorios/', relatorio.get_relatorio_all, name='listar_relatorios'),
    path('relatorios/add/', relatorio.post_relatorio, name='inserir_relatorio'),
    path('relatorios/update/<int:id>/', relatorio.delete_relatorio, name='deletar_relatorio'), 
    
    # Dashboard CRUD:
    path('dashboard/', dashboard.get_dashboard, name='listar_dashboard'),
    path('dashboard/add/', dashboard.post_dashboard, name='inserir_dashboard'),
    path('dashboard/update/<int:id>/', dashboard.update_dashboard, name="atualizar_dashboard"),
    path('dashboard/delete/<int:id>/', dashboard.delete_dashboard, name='deletar_dashboard'),
    
    # Log de Estoque:
    path('log_estoque/', logEstoque.get_movimentoEstoque_all, name='listar_log_estoque'),
    path('log_estoque/delete/<int:id>/', logEstoque.delete_movimentoEstoque, name='deletar_movimentoEstoque')
    
]


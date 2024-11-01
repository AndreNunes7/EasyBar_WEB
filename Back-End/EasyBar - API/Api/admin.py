from django.contrib import admin
from .Models.cadastros import Cadastro
from .Models.logEstoque import MovimentacaoEstoque
from .Models.pagamentos import Pagamento
from .Models.basic_model import Base
from .Models.produtos import Produto
from .Models.receita import Receita
from .Models.despesas import Despesa
from .Models.financeiro import Financeiro
from .Models.fornecedores import Fornecedor
from .Models.relatorio import Relatorio

@admin.register(Cadastro)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'cargo', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'cargo')
    list_filter = ('cargo', 'is_active')
    ordering = ('username',)



@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'quantidade_estoque', 'fornecedor', 'data_validade')
    search_fields = ('nome', 'categoria', 'fornecedor__nome')
    list_filter = ('categoria', 'fornecedor', 'data_validade')
    ordering = ('nome',)



@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'valor_total', 'data', 'descricao')
    search_fields = ('produto__nome', 'descricao')
    list_filter = ('data', 'produto')
    ordering = ('data',)

@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'data', 'categoria')
    search_fields = ('descricao', 'categoria')
    list_filter = ('categoria', 'data')
    ordering = ('data',)

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('fornecedor', 'produto', 'valor_pago', 'metodo_pagamento', 'data_pagamento', 'descricao')
    search_fields = ('fornecedor__nome', 'produto__nome', 'descricao')
    list_filter = ('metodo_pagamento', 'data_pagamento', 'fornecedor')
    ordering = ('-data_pagamento',)

@admin.register(MovimentacaoEstoque)
class LogMovimentoEstoqueAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'tipo_movimentacao', 'data_movimentacao', 'descricao')
    search_fields = ('produto__nome', 'descricao')
    list_filter = ('tipo_movimentacao', 'data_movimentacao', 'produto')
    ordering = ('-data_movimentacao',)


@admin.register(Financeiro)
class FinanceiroAdmin(admin.ModelAdmin):
    list_display = ('total_lucro', 'total_despesas', 'data', 'lucro')
    list_filter = ('data', 'lucro')
    ordering = ['-data']
    
    
    
@admin.register(Relatorio)
class RelatorioAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'data_inicio', 'data_fim')
    list_filter = ('tipo', 'data_inicio', 'data_fim')
    ordering = ['-data_inicio']
    
    
    
@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'data_cadastro')
    list_filter = ('nome',)
    ordering = ['-data_cadastro']
    
    
    
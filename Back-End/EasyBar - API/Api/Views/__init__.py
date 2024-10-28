import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..Models.usuarios import Usuario
from ..Models.despesas import Despesa
from ..Models.pagamentos import Pagamento
from ..Models.receita import Receita
from ..Models.produtos import Produto
from ..Models.dashboard import Dashboard
from ..Models.financeiro import Financeiro
from ..Models.logEstoque import MovimentacaoEstoque
from ..Models.fornecedores import Fornecedor
from ..Models.relatorio import Relatorio


# mexer aqui
from ..serializer import UserSerializer, DespesasSerializer, ReceitasSerializer, PagamentoSerializer, DashboardSerializer,\
    ProdutoSerializer, FornecedorSerializer, FinanceiroSerializer, RelatorioSerializer, MovimentoEstoqueSerializer
    
    
from .usuarios import get_users_all, post_user
from .receitas import get_receitas_all, post_receitas
from .despesas import get_despesas_all, post_despesa
from .pagamentos import get_pagamentos_fornecedores_all, post_pagamentos
from .produtos import get_produtos_all, post_produtos
from .financeiro import get_financas_all,post_financas
from .dashboard import get_dashboard, post_dashboard
from .fornecedores import get_fornecedores_all, post_fornecedor
from .relatorio import get_relatorio_all, post_relatorio
from .logEstoque import get_movimentoEstoque_all

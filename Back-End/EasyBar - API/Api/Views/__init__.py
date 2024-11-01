import json

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from ..Models.cadastros import Cadastro
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
from ..serializer import CadastroSerializer, DespesasSerializer, ReceitasSerializer, PagamentoSerializer, DashboardSerializer,\
    ProdutoSerializer, FornecedorSerializer, FinanceiroSerializer, RelatorioSerializer, MovimentoEstoqueSerializer
    
    
from .cadastros import cadastrar, get_cadastros_all
from .receitas import get_receitas_all, post_receitas, delete_receitas, update_receitas
from .despesas import get_despesas_all, post_despesa, delete_despesa, update_despesa
from .pagamentos import get_pagamentos_fornecedores_all, post_pagamentos, delete_pagamento, update_pagamento
from .produtos import get_produtos_all, post_produtos, update_produto, delete_produto
from .financeiro import get_financas_all,post_financas, delete_financa, update_financa
from .dashboard import get_dashboard, post_dashboard, delete_dashboard, update_dashboard
from .fornecedores import get_fornecedores_all, post_fornecedor, delete_fornecedor, update_fornecedor
from .relatorio import get_relatorio_all, post_relatorio, delete_fornecedor, update_fornecedor
from .logEstoque import get_movimentoEstoque_all, delete_movimentoEstoque

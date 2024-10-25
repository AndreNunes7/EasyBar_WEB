import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..Models.usuarios_model import Usuarios
from ..Models.despesas_model import Despesa
from ..Models.mesa_model import Mesa
from ..Models.pagamentos_model import PagamentoFornecedor
from ..Models.receita_model import Receita
from ..Models.produto_model import Produto
from ..Models.logAcao_model import LogAcao



from ..serializer import UserSerializer, ProductSerializer, DespesasSerializer, ReceitasSerializer, MesaSerializer, PagamentoFornecedorSerializer

from .usuarios_views import get_users_all, post_user
from .receitas_views import get_receitas_all, post_receitas
from .despesas_views import get_despesas_all, post_despesa
from .pagamentos_views import get_pagamentos_fornecedores_all, post_pagamentos
from .mesas_views import get_mesas_all, post_mesa
from .produtos_views import get_produtos_all, post_produtos

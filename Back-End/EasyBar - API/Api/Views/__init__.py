import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Usuarios, Produto, Despesa, Receita, Mesa, Pagamento
from ..serializer import UserSerializer, ProductSerializer, DespesasSerializer, ReceitasSerializer, MesaSerializer, PagamentoComandaSerializer

from .usuarios_views import get_users_all
from .receitas_views import get_receitas_all
from .despesas_views import get_despesas_all
from .pagamentos_views import get_pagamentos_comanda_all
from .mesas_views import get_mesas_all
from .produtos_views import get_products_all

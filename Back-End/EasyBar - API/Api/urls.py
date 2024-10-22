from django.contrib import admin
from django.urls import path, include
from .Views import *

from . import Views

urlpatterns = [
    path('users/', Views.get_users_all, name='get_all_users'),
    path('produtos/', Views.get_products_all, name='get_all_products'),  
    path('despesas/', Views.get_despesas_all, name='get_all_despesas'),
    path('receitas/', Views.get_receitas_all, name='get_all_receitas'),
    path('pagamentos/', Views.get_pagamentos_comanda_all, name='get_all_pagamentos'),
]


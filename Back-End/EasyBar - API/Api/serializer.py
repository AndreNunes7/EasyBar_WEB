from rest_framework import serializers
from .Models import *
"""
Get all users:   

Examples:

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'  
"""
     
     
"""
Get User specific information:

Examples: 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['id', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined', 'cargo']
"""
     
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'is_active', 'is_staff', 'cargo']

        extra_kwargs = {
            'username': {'required': True, 'allow_blank': False},
            'cargo': {'required': False},
        }

    def valida_username(self, nome):
        if nome.isdigit():
            raise serializers.ValidationError("O nome de usuário não pode conter apenas dígitos")
        
        if ' ' in nome:
            raise serializers.ValidationError("O nome de usuário não pode conter espaço em branco")
        
        return nome


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
        
        

class DespesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'
        
        
        
class ReceitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'
        
       
        
class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ['id', 'nome', 'documento', 'endereco', 'telefone', 'email']


class PagamentoSerializer(serializers.ModelSerializer):
    fornecedor = FornecedorSerializer() 

    class Meta:
        model = Pagamento
        fields = ['fornecedor', 'produto', 'descricao', 'metodo_pagamento', 'valor_pago', 'data_pagamento']
        
        
        
class RelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relatorio
        fields = '__all__',
        
        
class FinanceiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financeiro
        fields = '__all__'
        
        
        
class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = '__all__'
        
        
class MovimentoEstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimentacaoEstoque
        fields = '__all__'
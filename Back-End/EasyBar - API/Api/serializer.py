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
        model = Usuarios
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


class ProductSerializer(serializers.ModelSerializer):
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
        
       
       
class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'
        
        
        
class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ['id', 'nome', 'documento', 'endereco', 'telefone', 'email']

class PagamentoFornecedorSerializer(serializers.ModelSerializer):
    fornecedor = FornecedorSerializer()  # Inclui informações do fornecedor

    class Meta:
        model = PagamentoFornecedor
        fields = ['fornecedor', 'descricao', 'metodo_pagamento', 'valor_pago', 'data_pagamento']
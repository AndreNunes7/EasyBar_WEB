from django.forms import ValidationError
from rest_framework import serializers

from Api.Auth.validators import UnicodeUsernameValidator
from .Models import *
from .Auth import valida_password
from django.contrib.auth.hashers import make_password

"""
Get all users:   

Examples:

class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastros
        fields = '__all__'  
"""
     
     
"""
Get User specific information:

Examples: 

class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastros
        fields = ['id', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined', 'cargo']
"""
     
        


class CadastroSerializer(serializers.ModelSerializer):
    username_validator = UnicodeUsernameValidator()

    class Meta:
        model = Cadastro
        fields = ['username', 'password', 'papel', 'cargo', 'telefone']


    def validate_username(self, value):
        self.username_validator(value)

        if value.isdigit():
            raise serializers.ValidationError("O nome de usuário não pode conter apenas dígitos")
        
        if ' ' in value:
            raise serializers.ValidationError("O nome de usuário não pode conter espaços em branco")
        
        return value
    def validate_password(self, value):
        username = self.initial_data.get('username')  
        try:
            valida_password(value, username=username) 
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)








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
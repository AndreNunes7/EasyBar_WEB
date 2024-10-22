from rest_framework import serializers
from .models import Usuarios, Produto, Despesa, Receita, Mesa, Pagamento

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
        fields = ['id', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined', 'cargo']
        
        

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
        
        

class PagamentoComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ['Comanda.mesa', 'valor_total', 'produtos']
from rest_framework import serializers
from .models import Usuarios


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'
        
   
        
# class UserStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Usuarios
#         fields = ['status']
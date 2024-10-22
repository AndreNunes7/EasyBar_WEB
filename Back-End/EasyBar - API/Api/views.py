from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Usuarios
from .serializer import UserSerializer

import json


# inserir: Usuarios.objects.get(pk=username) -> retorna OBJETO
# consulta: Usuarios.objects.filter(username=username) -> retorna QUERYSET
# delete: Usuarios.delete() 
# consulta sem o parametro que passarmos: Usuarios.objects.exclude(username='André') -> retorna um objeto em que o nome não é 'André', -> retorna um queryset
# save: Usuarios.save() 



# GET:

@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = Usuarios.objects.all()  # <--- Pega todos os objetos
        serializer = UserSerializer(users, many=True) # <-- Serializa o objeto, many: diz para pegar todos os objetos
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
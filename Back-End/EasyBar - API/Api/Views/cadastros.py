from . import *
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..Models import Cadastro
from ..serializer import CadastroSerializer



@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_cadastros_all(request):
    if request.method == 'GET':
        users = Cadastro.objects.all() 
        serializer = CadastroSerializer(users, many=True)  
        tokens = [
            {
                'user': user.username,  
                'refresh': str(RefreshToken.for_user(user)),
                'access': str(RefreshToken.for_user(user).access_token),
            }
            for user in users
        ]
        
        return Response({'users': serializer.data, 'tokens': tokens}, status=status.HTTP_200_OK)


@api_view(['POST'])
def cadastrar(request):
    if request.method == 'POST':
        serializer = CadastroSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



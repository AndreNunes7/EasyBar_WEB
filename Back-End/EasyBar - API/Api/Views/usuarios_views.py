from . import *



@api_view(['GET'])
def get_users_all(request):
    if request.method == 'GET':
        users = Usuarios.objects.all()  # <--- Pega todos os objetos
        serializer = UserSerializer(users, many=True) # <-- Serializa o objeto, many: diz para pegar todos os objetos
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
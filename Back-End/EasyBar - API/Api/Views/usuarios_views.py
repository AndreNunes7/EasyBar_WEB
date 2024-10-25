from . import *



@api_view(['GET'])
def get_users_all(request):
    if request.method == 'GET':
        users = Usuarios.objects.all()  # <--- Pega todos os objetos
        serializer = UserSerializer(users, many=True) # <-- Serializa o objeto, many: diz para pegar todos os objetos
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
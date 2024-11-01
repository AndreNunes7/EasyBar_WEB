from . import *

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_receitas_all(request):
    if request.method == 'GET':
        receitas = Receita.objects.all()
        serializer = ReceitasSerializer(receitas, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def post_receitas(request):
    if request.method == 'POST':
        serializer = ReceitasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_receitas(request, id):
    if request.method == 'PUT':
        receita = Receita.objects.get(id=id)
        serializer = ReceitasSerializer(receita, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_receitas(request, id):
    if request.method == 'DELETE':
        receita = Receita.objects.get(id=id)
        receita.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
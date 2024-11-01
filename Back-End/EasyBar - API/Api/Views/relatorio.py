from . import *

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_relatorio_all(request):
    if request.method == 'GET':
        relatorio = Relatorio.objects.all()
        serializer = RelatorioSerializer(relatorio, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def post_relatorio(request):
    if request.method == 'POST':
        serializer = RelatorioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_relatorio(request,id):
    if request.method == 'DELETE':
        relatorio = Relatorio.objects.get(id=id)
        relatorio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(relatorio.errors, status=status.HTTP_400_BAD_REQUEST)
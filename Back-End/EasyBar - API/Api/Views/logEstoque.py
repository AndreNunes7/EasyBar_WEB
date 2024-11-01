from . import *

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_movimentoEstoque_all(request):
    if request.method == 'GET':
        movimento = MovimentacaoEstoque.objects.all()
        serializer = MovimentoEstoqueSerializer(movimento, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_movimentoEstoque(request, id):
    if request.method == 'DELETE':
        movimento = MovimentacaoEstoque.objects.get(id=id)
        movimento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    
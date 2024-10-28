from . import *

@api_view(['GET'])
def get_movimentoEstoque_all(request):
    if request.method == 'GET':
        movimento = MovimentacaoEstoque.objects.all()
        serializer = MovimentoEstoqueSerializer(movimento, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

   
from . import *

@api_view(['GET'])
def get_products_all(request):
    if request.method == 'GET':
        produtos = Produto.objects.all() 
        serializer = ProductSerializer(produtos, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

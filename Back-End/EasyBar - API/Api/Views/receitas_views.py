from . import *

@api_view(['GET'])
def get_receitas_all(request):
    if request.method == 'GET':
        receitas = Receita.objects.all()
        serializer = ReceitasSerializer(receitas, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
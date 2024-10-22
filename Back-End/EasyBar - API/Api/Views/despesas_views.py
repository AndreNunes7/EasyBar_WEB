from . import *

@api_view(['GET'])
def get_despesas_all(request):
    if request.method == 'GET':
        despesas = Despesa.objects.all()
        serializer = DespesasSerializer(despesas, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
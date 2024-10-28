from . import *

@api_view(['GET'])
def get_despesas_all(request):
    if request.method == 'GET':
        despesas = Despesa.objects.all()
        serializer = DespesasSerializer(despesas, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_despesa(request):
    if request.method == 'POST':
        serializer = DespesasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
   
from . import *

@api_view(['GET'])
def get_pagamentos_comanda_all(request):
    if request.method == 'GET':
        pagamentos = Pagamento.objects.all()
        serializer = PagamentoComandaSerializer(pagamentos, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
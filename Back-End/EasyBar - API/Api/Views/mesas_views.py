from . import *

@api_view(['GET'])
def get_mesas_all(request):
    if request.method == 'GET':
        mesas = Mesa.objects.all()
        serializer = MesaSerializer(mesas, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
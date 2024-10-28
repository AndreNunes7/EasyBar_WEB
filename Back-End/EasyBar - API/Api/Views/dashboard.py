from . import *

@api_view(['GET'])
def get_dashboard(request):
    if request.method == 'GET':
        dashboard = Dashboard.objects.all()
        serializer = DashboardSerializer(dashboard, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_dashboard(request):
    if request.method == 'POST':
        serializer = DashboardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
   
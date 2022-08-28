from rest_framework import viewsets
from .serializers import MytableSerializer
from .models import Mytable
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def table(request):
	queryset = Mytable.objects.all().order_by('id')[:10]
	serializer = MytableSerializer(queryset, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def table_detail(request, id):
    table = Mytable.objects.get(pk=id)
    serializer = MytableSerializer(table, many=False)
    return Response(serializer.data)
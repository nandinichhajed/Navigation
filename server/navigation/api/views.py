from rest_framework import viewsets
from .serializers import MytableSerializer
from .models import Mytable
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import mixins, viewsets

# Create your views here.

class MytableViewSet(viewsets.ModelViewSet):
    queryset = Mytable.objects.all().order_by('ID')[:10]
    serializer_class = MytableSerializer

# class MyTableAPIView(mixins.ListModelMixin, viewsets.GenericViewSet):
#     serializer_class = MytableSerializer

#     def get_queryset(self):
#         my_tables = Mytable.objects.all().order_by('ID')[:10]
#         return my_tables

#     def get(self, request, *args, **kwargs):
        
#         try:
#             id = request.query_params["id"]
#             if id != None:
#                 my_table = Mytable.objects.get(id=id)
#                 serializer = MytableSerializer(my_table)
#         except:
#             my_tables = self.get_queryset()
#             serializer = MytableSerializer(my_tables, many=True)

#         return Response(serializer.data)
from rest_framework import viewsets
from .serializers import MytableSerializer
from .models import Mytable
# Create your views here.

class MytableViewSet(viewsets.ModelViewSet):
    queryset = Mytable.objects.all().order_by('ID')[:10]
    serializer_class = MytableSerializer

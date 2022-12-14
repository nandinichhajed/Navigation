from rest_framework import serializers
from .models import Mytable

class MytableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mytable
        fields = ('id','Course_Over_Ground', 'Latitude', 'Longitude', 'Ship_ID', 'Speed', 'Time')
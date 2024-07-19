from rest_framework import serializers
from .models import Itemlist

class itemserializers(serializers.ModelSerializer):
    class Meta:
        model=Itemlist
        fields='__all__'
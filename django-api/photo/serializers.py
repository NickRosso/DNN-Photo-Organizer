from rest_framework import serializers
from .models import Photo

class photoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'created_date', 'path', 'classification']
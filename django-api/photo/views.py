from django.shortcuts import render
from rest_framework import viewsets
from .models import Photo
from .serializers import photoSerializer

# Create your views here.
class PhotoViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = Photo_Serializer
    queryset = Photo.objects.all()
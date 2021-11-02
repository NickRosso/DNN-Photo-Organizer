from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Photo
from .serializers import photoSerializer
from .tasks import classify_photo

class PhotoViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = photoSerializer
    queryset = Photo.objects.all()

    def create(self, request, *args, **kwargs):
        serialized_photo_object = self.get_serializer(data=request.data)
        serialized_photo_object.is_valid(raise_exception=True)
        self.perform_create(serialized_photo_object)
        headers = self.get_success_headers(serialized_photo_object.data)
        return Response(serialized_photo_object.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serialized_photo_object):
        serialized_photo_object.save()
        print(serialized_photo_object.data)
        #classify_photo.apply_async(args=[serialized_photo_object.data["id"]])
        classify_photo(serialized_photo_object.data["id"])
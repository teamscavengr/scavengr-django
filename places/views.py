from dataaccess.models import Place
from dataaccess.serializers import PlaceSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


class Places(APIView):
    #permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Place.objects.get(pk=pk)
        except Place.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk is None:
            # List all Places
            places = Place.objects.all()
            serializer = PlaceSerializer(places, many=True)
            return Response(serializer.data)
        else:
            place = self.get_object(pk)
            serializer = PlaceSerializer(place)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        place = self.get_object(pk)
        serializer = PlaceSerializer(place,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
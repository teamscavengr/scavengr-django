from dataaccess.models import Profile
from django.contrib.auth.models import User
from dataaccess.serializers import ProfileSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


class Users(APIView):
    # permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return User.objects.get(username=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk is None:
            # List all Users
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        else:
            # retrieve one user
            user = self.get_object(pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)

    def put(self, request, pk=None, format=None):
        user = self.get_object(pk)
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            #create profile with link to user and save
            serializer.create(user, serializer.validated_data).save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

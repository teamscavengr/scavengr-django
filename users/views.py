from dataaccess.models import User
from dataaccess.serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


class Users(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk is None:
            #List all Users
            snippets = User.objects.all()
            serializer = UserSerializer(snippets, many=True)
            return Response(serializer.data)
        else:
            #retrieve one user
            snippet = self.get_object(pk)
            serializer = UserSerializer(snippet)
            return Response(serializer.data)

    def post(self, request, pk=None, format=None):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(owner = self.request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        snippet = self.get_object(pk)
        serializer = UserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        if pk is None:
            return Response("Please select a single object to delete")
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
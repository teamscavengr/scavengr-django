from rest_framework import serializers
from dataaccess.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','profile_pic','created','modified','owner')
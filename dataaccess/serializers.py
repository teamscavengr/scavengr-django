from rest_framework import serializers
from django.contrib.auth.models import User
from dataaccess.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_pic',)

    def create(self, user, validated_data):
        return Profile(user=user, **validated_data)


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'profile')

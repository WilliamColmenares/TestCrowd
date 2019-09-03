from rest_framework import serializers
from pets.models import Pet
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """This is just to show username too not just the id"""
    class Meta:
        model = User
        fields = ('id', 'username')


class PetSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Pet
        fields = '__all__'

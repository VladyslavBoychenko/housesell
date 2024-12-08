from rest_framework import serializers
from .models import UserSerializer

class UserqSerializer(serializers. ModelSerializer):
    class Meta:
        model = UserSerializer
        fields = '_all_'
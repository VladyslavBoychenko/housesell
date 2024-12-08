from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import models
from main.models import User, Apartment, House


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'is_admin']

# Серіалізатор для квартири
class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ['title', 'description', 'area', 'price', 'rooms', 'floor', 'category', 'date_published', 'owner']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(representation)  # Логування результатів серіалізації
        return representation


# Серіалізатор для будинку
class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['title', 'description', 'area', 'price', 'rooms', 'garage', 'category', 'date_published', 'owner']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(representation)  # Логування результатів серіалізації
        return representation

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers
from .models import User, Apartment, House, UserSerializer, ApartmentSerializer, HouseSerializer
from rest_framework import status

@api_view(['GET'])
def getData(request):
    # Отримуємо всіх користувачів
    users = User.objects.all()

    # Створюємо списки для результатів
    all_users_data = []

    # Для кожного користувача отримуємо квартири та будинки
    for user in users:
        apartments = Apartment.objects.filter(owner=user)
        houses = House.objects.filter(owner=user)

        # Серіалізуємо дані
        user_serializer = UserSerializer(user)
        apartment_serializer = ApartmentSerializer(apartments, many=True)
        house_serializer = HouseSerializer(houses, many=True)

        # Додаємо серіалізовані дані в список
        all_users_data.append({
            'user': user_serializer.data,
            'apartments': apartment_serializer.data,
            'houses': house_serializer.data
        })

    # Повертаємо всі дані у відповіді
    return Response(all_users_data)

@api_view(['POST'])
def addApartment(request):
    if request.method == 'POST':
        serializer = ApartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Зберігаємо нову квартиру
            return Response(serializer.data, status=201)  # Повертаємо серіалізовані дані нової квартири
        return Response(serializer.errors, status=400)


# Функція для додавання нового будинку
@api_view(['POST'])
def addHouse(request):
    if request.method == 'POST':
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Зберігаємо новий будинок
            return Response(serializer.data, status=201)  # Повертаємо серіалізовані дані нового будинку
        return Response(serializer.errors, status=400)


# Функція для додавання нового користувача
@api_view(['POST'])
def addUser(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Зберігаємо нового користувача
            return Response(serializer.data, status=201)  # Повертаємо серіалізовані дані нового користувача
        return Response(serializer.errors, status=400)



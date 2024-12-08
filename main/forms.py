from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import House
from .models import Apartment
from django.forms import ModelForm
from .models import Property
from .models import Apartment, House, PropertyCategory
from .models import User

class ApartmentSearchForm(forms.Form):
    # Фільтрація за площею
    AREA_CHOICES = [
        ('', 'Оберіть площу'),  # Порожнє значення для за замовчуванням
        ('0-45', '0 - 45 м²'),
        ('45-90', '45 - 90 м²'),
        ('90+', '90 м² і більше'),
    ]
    area = forms.ChoiceField(choices=AREA_CHOICES, required=False, label='Площа')

    # Фільтрація за ціною
    PRICE_CHOICES = [
        ('', 'Оберіть ціну'),  # Порожнє значення для за замовчуванням
        ('0-100000', '0 - 100,000 $'),
        ('100000-200000', '100,000 - 200,000 $'),
        ('200000+', '200,000 $ і більше'),
    ]
    price = forms.ChoiceField(choices=PRICE_CHOICES, required=False, label='Ціна')

    # Фільтрація за кількістю кімнат
    ROOMS_CHOICES = [
        ('', 'Оберіть кількість кімнат'),  # Порожнє значення для за замовчуванням
        ('1', '1 кімната'),
        ('2', '2 кімнати'),
        ('3', '3 кімнати'),
        ('4+', '4 і більше'),
    ]
    rooms = forms.ChoiceField(choices=ROOMS_CHOICES, required=False, label='Кількість кімнат')

    # Фільтрація за поверхами
    FLOOR_CHOICES = [
        ('', 'Оберіть поверхи'),  # Порожнє значення для за замовчуванням
        ('1-5', '1 - 5 поверхи'),
        ('5-10', '5 - 10 поверхи'),
        ('10-15', '10 - 15 поверхи'),
        ('15+', '15 і більше поверхів'),
    ]
    floor = forms.ChoiceField(choices=FLOOR_CHOICES, required=False, label='Поверхи')

class HouseSearchForm(forms.Form):
    # Фільтрація за площею
    AREA_CHOICES = [
        ('', 'Оберіть площу'),
        ('0-45', '0 - 45 м²'),
        ('45-90', '45 - 90 м²'),
        ('90+', '90 м² і більше'),
    ]
    area = forms.ChoiceField(choices=AREA_CHOICES, required=False, label='Площа')

    # Фільтрація за ціною
    PRICE_CHOICES = [
        ('', 'Оберіть ціну'),
        ('0-100000', '0 - 100,000 $'),
        ('100000-200000', '100,000 - 200,000 $'),
        ('200000+', '200,000 $ і більше'),
    ]
    price = forms.ChoiceField(choices=PRICE_CHOICES, required=False, label='Ціна')

    # Фільтрація за кількістю кімнат
    ROOMS_CHOICES = [
        ('', 'Оберіть кількість кімнат'),
        ('1', '1 кімната'),
        ('2', '2 кімнати'),
        ('3', '3 кімнати'),
        ('4+', '4 і більше'),
    ]
    rooms = forms.ChoiceField(choices=ROOMS_CHOICES, required=False, label='Кількість кімнат')

    # Фільтрація за наявністю гаражу
    GARAGE_CHOICES = [
        ('', 'Оберіть наявність гаражу'),
        ('1 - 99', 'З гаражем'),
        ('0', 'Без гаражу'),
    ]
    garage = forms.ChoiceField(choices=GARAGE_CHOICES, required=False, label='Наявність гаражу')


# Форма для квартири
class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['area', 'floor', 'price', 'title', 'description', 'image', 'category', 'rooms']
        widgets = {
            'area': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Площа м²', 'required': True}),
            'floor': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ціна', 'required': True}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Назва'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Опис'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'rooms': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Кількість кімнат', 'required': True})  # Додано поле для кількості кімнат
        }


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['area', 'garage', 'price', 'title', 'description', 'image', 'category', 'rooms']
        widgets = {
            'area': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Площа м²', 'required': True}),
            'garage': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ціна', 'required': True}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Назва'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Опис'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'rooms': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Кількість кімнат', 'required': True})  # Додано поле для кількості кімнат
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label='Логін',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        label='Номер телефону',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=15,  # Обмеження на максимальну кількість символів (можна змінити)
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Повтор пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Логін',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'profile_picture']


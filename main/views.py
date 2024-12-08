from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.apps import apps
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404
from .models import Apartment
from .forms import ApartmentSearchForm, RegisterUserForm, LoginUserForm, ApartmentForm, HouseForm, UserProfileForm
from .models import House
from .forms import HouseSearchForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import DetailView



def index(request):
    apartments = Apartment.objects.all()  # Якщо ви хочете вивести всі квартири
    houses = House.objects.all()  # Якщо ви хочете вивести всі будинки

    return render(request, 'main/home.html', {
        'title': 'HouseSell - придбай житло власної мрії',
        'apartment': apartments[0] if apartments else None,
        'house': houses[0] if houses else None,
        'apartment_2': apartments[1] if len(apartments) > 1 else None,
        'house_2': houses[1] if len(houses) > 1 else None,
        'apartment_3': apartments[2] if len(apartments) > 2 else None,  # Додаємо 3-ю квартиру
    })



def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


def buy(request):
    apartments = Apartment.objects.all()

    # Отримання значень з форми
    form = ApartmentSearchForm(request.GET)

    # Фільтрація за площею
    area_filter = request.GET.get('area')
    if area_filter == '0-45':
        apartments = apartments.filter(area__lte=45)
    elif area_filter == '45-90':
        apartments = apartments.filter(area__gt=45, area__lte=90)
    elif area_filter == '90+':
        apartments = apartments.filter(area__gt=90)

    # Фільтрація за ціною
    price_filter = request.GET.get('price')
    if price_filter == '0-100000':
        apartments = apartments.filter(price__lte=100000)
    elif price_filter == '100000-200000':
        apartments = apartments.filter(price__gt=100000, price__lte=200000)
    elif price_filter == '200000+':
        apartments = apartments.filter(price__gt=200000)

    # Фільтрація за кількістю кімнат
    rooms_filter = request.GET.get('rooms')
    if rooms_filter == '1':
        apartments = apartments.filter(rooms=1)
    elif rooms_filter == '2':
        apartments = apartments.filter(rooms=2)
    elif rooms_filter == '3':
        apartments = apartments.filter(rooms=3)
    elif rooms_filter == '4+':
        apartments = apartments.filter(rooms__gte=4)

    # Фільтрація за поверхами
    floor_filter = request.GET.get('floor')
    if floor_filter == '1-5':
        apartments = apartments.filter(floor__gte=1, floor__lte=5)
    elif floor_filter == '5-10':
        apartments = apartments.filter(floor__gte=5, floor__lte=10)
    elif floor_filter == '10-15':
        apartments = apartments.filter(floor__gte=10, floor__lte=15)
    elif floor_filter == '15+':
        apartments = apartments.filter(floor__gte=15)

    return render(request, 'main/buy.html', {'buy': apartments, 'form': form})


def sell(request):
    error = ''

    if request.method == 'POST':
        # Перевірка, чи це форма для квартири
        if 'apartment' in request.POST:
            form = ApartmentForm(request.POST, request.FILES)
            if form.is_valid():
                apartment = form.save(commit=False)
                apartment.rooms = apartment.rooms or 1  # Якщо rooms не вказано, встановлюємо за замовчуванням
                apartment.owner = request.user  # Встановлюємо поточного користувача як власника
                apartment.save()
                return redirect('home')
            else:
                error = "Форма була неправильною"

        # Перевірка, чи це форма для будинку
        elif 'house' in request.POST:
            form_house = HouseForm(request.POST, request.FILES)
            if form_house.is_valid():
                house = form_house.save(commit=False)
                house.rooms = house.rooms or 1  # Якщо rooms не вказано, встановлюємо за замовчуванням
                house.owner = request.user  # Встановлюємо поточного користувача як власника
                house.save()
                return redirect('home')
            else:
                error = "Форма була неправильною"

    else:
        form = ApartmentForm()
        form_house = HouseForm()

    data = {
        'form': form,
        'form_house': form_house,
        'error': error
    }

    return render(request, 'main/sell.html', data)



def buyhouse(request):
    house = House.objects.all()

    # Отримання значень з форми
    form = HouseSearchForm(request.GET)

    # Фільтрація за площею
    area_filter = request.GET.get('area')
    if area_filter == '0-45':
        house = house.filter(area__lte=45)
    elif area_filter == '45-90':
        house = house.filter(area__gt=45, area__lte=90)
    elif area_filter == '90+':
        house = house.filter(area__gt=90)

    # Фільтрація за ціною
    price_filter = request.GET.get('price')
    if price_filter == '0-100000':
        house = house.filter(price__lte=100000)
    elif price_filter == '100000-200000':
        house = house.filter(price__gt=100000, price__lte=200000)
    elif price_filter == '200000+':
        house = house.filter(price__gt=200000)

    # Фільтрація за кількістю кімнат
    rooms_filter = request.GET.get('rooms')
    if rooms_filter == '1':
        house = house.filter(rooms=1)
    elif rooms_filter == '2':
        house = house.filter(rooms=2)
    elif rooms_filter == '3':
        house = house.filter(rooms=3)
    elif rooms_filter == '4+':
        house = house.filter(rooms__gte=4)

    # Фільтрація за наявністю гаражу
    garage_filter = request.GET.get('garage')
    if garage_filter == '1':
        house = house.filter(garage=True)
    elif garage_filter == '0':
        house = house.filter(garage=False)
    # Якщо фільтр не вибрано, всі будинки без обмежень по гаражу
    elif garage_filter == '':
        pass

    return render(request, 'main/buyhouse.html', {'buy': house, 'form': form})

class ApartmentDetailView (DetailView):
    model = Apartment
    template_name = 'main/flat/flat.html'
    context_object_name = 'article'

class HousetDetailView (DetailView):
    model = House
    template_name = 'main/house/house.html'
    context_object_name = 'house'

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_user_context(title="Реєстрація"))
        return context

# Якщо є необхідність створювати функцію для реєстрації:
def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'main/register.html', {'form': form})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'  # Шаблон для сторінки входу
    success_url = reverse_lazy('home')  # Перенаправлення після успішного входу

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Авторизація"  # Додаємо свій контекст
        return context


def logout_user(request):
    logout(request)
    return redirect('home')  # Переадресація на сторінку входу після виходу




def profile(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)

    apartments = Apartment.objects.filter(owner=user)
    houses = House.objects.filter(owner=user)

    context = {
        'user': user,
        'form': form,
        'apartments': apartments,
        'houses': houses,
    }

    return render(request, 'main/profile.html', context)



def add_property(request):
    # Перевіряємо, чи користувач увійшов
    if not request.user.is_authenticated:
        return redirect('login')  # Перенаправляємо на сторінку логіну, якщо користувач не авторизований

    # Обробка форми для квартири
    if request.method == 'POST':
        if 'apartment' in request.POST:
            apartment_form = ApartmentForm(request.POST, request.FILES)
            if apartment_form.is_valid():
                apartment = apartment_form.save(commit=False)
                apartment.owner = request.user  # Призначаємо власника
                apartment.save()  # Зберігаємо квартиру
                return redirect('profile')  # Перенаправляємо на сторінку профілю

        # Обробка форми для будинку
        elif 'house' in request.POST:
            house_form = HouseForm(request.POST, request.FILES)
            if house_form.is_valid():
                house = house_form.save(commit=False)
                house.owner = request.user  # Призначаємо власника
                house.save()  # Зберігаємо будинок
                return redirect('profile')  # Перенаправляємо на сторінку профілю
    else:
        apartment_form = ApartmentForm()
        house_form = HouseForm()

    context = {
        'apartment_form': apartment_form,
        'house_form': house_form,
    }

    return render(request, 'main/profile.html', context)


def edit(request):
    if request.user.is_authenticated:
        apartments = Apartment.objects.filter(owner=request.user)
        houses = House.objects.filter(owner=request.user)

        if request.method == 'POST':
            ad_id = request.POST.get('ad_id')
            ad_model = request.POST.get('ad_model')

            # Обробка редагування оголошення
            if 'delete_ad' in request.POST:  # Перевірка на кнопку "Видалити"
                try:
                    Model = apps.get_model('main', ad_model)
                    ad = Model.objects.filter(id=ad_id, owner=request.user).first()

                    if ad:
                        ad.delete()
                        messages.success(request, 'Оголошення успішно видалено.')
                    else:
                        messages.error(request, 'Оголошення не знайдено або відсутній доступ.')

                except LookupError:
                    messages.error(request, 'Некоректна модель оголошення.')

            else:  # Обробка оновлення оголошення
                try:
                    Model = apps.get_model('main', ad_model)
                    ad = Model.objects.filter(id=ad_id, owner=request.user).first()

                    if ad:
                        ad.title = request.POST.get('title', ad.title)
                        ad.price = request.POST.get('price', ad.price)
                        ad.area = request.POST.get('area', ad.area)
                        ad.rooms = request.POST.get('rooms', ad.rooms)

                        if hasattr(ad, 'garage'):
                            ad.garage = request.POST.get('garage', ad.garage)

                        if hasattr(ad, 'floor'):
                            ad.floor = request.POST.get('floor', ad.floor)

                        if 'image' in request.FILES:
                            ad.image = request.FILES['image']

                        ad.save()
                        messages.success(request, 'Оголошення успішно оновлено.')
                    else:
                        messages.error(request, 'Оголошення не знайдено або відсутній доступ.')

                except LookupError:
                    messages.error(request, 'Некоректна модель оголошення.')

            return redirect('edit')

        context = {
            'apartments': apartments,
            'houses': houses,
        }
        return render(request, 'main/edit.html', context)

    else:
        messages.error(request, 'Будь ласка, увійдіть, щоб редагувати оголошення.')
        return redirect('login')

def apartment_detail(request, id):
    apartment = get_object_or_404(Apartment, id=id)
    owner = apartment.owner  # Отримуємо власника квартири
    return render(request, 'main/flat/flat.html', {
        'apartment': apartment,
        'owner': owner,  # Передаємо власника
    })

def house_detail(request, id):
    house = get_object_or_404(House, id=id)
    owner = house.owner  # Отримуємо власника квартири
    return render(request, 'main/house/house.html', {
        'house': house,
        'owner': owner,  # Передаємо власника
    })




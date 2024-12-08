from django.db import models
from django.contrib.auth.models import AbstractUser

# Користувач
class User(AbstractUser):
    phone_number = models.CharField('Номер телефону', max_length=15, blank=True, null=True)
    is_admin = models.BooleanField('Чи є адміністратором', default=False)
    profile_picture = models.ImageField('Фото профілю', upload_to='profile_pictures/', blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='Групи, до яких належить користувач.',
        verbose_name='Групи'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Спеціальні дозволи для користувача.',
        verbose_name='Дозволи'
    )

    def __str__(self):
        return self.username

# Загальна категорія нерухомості
class PropertyCategory(models.Model):
    name = models.CharField('Категорія', max_length=50)

    def __str__(self):
        return self.name

# Абстрактна модель для спільних полів нерухомості
class Property(models.Model):
    title = models.CharField('Назва', max_length=100)
    description = models.TextField('Опис')
    area = models.FloatField('Площа (м²)')
    price = models.DecimalField('Ціна', max_digits=12, decimal_places=2)
    rooms = models.IntegerField('Кількість кімнат')
    category = models.ForeignKey(
        PropertyCategory, on_delete=models.CASCADE, related_name='%(class)s_category'
    )
    date_published = models.DateTimeField('Дата публікації', auto_now_add=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='%(class)s_owner'
    )
    image = models.ImageField('Зображення', upload_to='property_images/', blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

# Квартира
# Квартира
class Apartment(Property):
    floor = models.IntegerField('Поверх')
    rooms = models.IntegerField('Кількість кімнат', default=1)  # Додано поле для кількості кімнат

# Будинок
class House(Property):
    garage = models.IntegerField('Гараж')
    rooms = models.IntegerField('Кількість кімнат', default=1)  # Додано поле для кількості кімнат

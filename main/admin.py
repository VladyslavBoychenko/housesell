from django.contrib import admin
from .models import User,  Apartment, House

admin.site.register(User)
admin.site.register(Apartment)
admin.site.register(House)
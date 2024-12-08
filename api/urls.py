from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('addhouse/', views.addHouse),
    path('adduser/', views.addUser),
    path('addapart/', views.addApartment),
    ]
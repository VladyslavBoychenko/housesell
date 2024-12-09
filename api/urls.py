from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('api/addhouse/', views.addHouse),
    path('api/adduser/', views.addUser),
    path('api/addapart/', views.addApartment),
    ]
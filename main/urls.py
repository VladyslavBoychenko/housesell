from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='home'),
    #path('', include('api.urls')),
    path('<int:pk>', views.ApartmentDetailView.as_view(), name='flat'),
    path('apartment/<int:id>/', views.apartment_detail, name='apartment_detail'),
    path('house/<int:id>/', views.house_detail, name='house_detail'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('buy', views.buy, name='buy'),
    path('sell', views.sell, name='sell'),
    path('buyhouse', views.buyhouse, name='buyhouse'),
    path('register', views.register, name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit/', views.edit, name='edit')
]

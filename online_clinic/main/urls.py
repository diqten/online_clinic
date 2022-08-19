from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('index_page', views.index_page, name='index_page'),
    path('doctors', views.doctors_page, name='doctors'),
    path('price', views.price_page, name='price'),
    path('contacts', views.contacts_page, name='contacts'),
    path('login', views.login_page, name='login'),
    path('register', views.register_page, name='register'),
    path('profile', views.profile_page, name='profile'),
    path('logout', views.logout_view, name='logout_view'),
    path('zapic', views.zapic_page, name='zapic'),
]
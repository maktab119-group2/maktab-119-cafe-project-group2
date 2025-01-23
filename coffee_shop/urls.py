from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]
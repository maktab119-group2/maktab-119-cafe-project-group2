from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='login'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('menu/', menu, name='menu'),
    path('add/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='cart'),
    path('order/', order_view, name='order'),
    path('create_order/', create_order, name='create_order'),
    path('mark_order_ready/<int:order_id>/', mark_order_ready, name='mark_order_ready'),
    path('receipt/', receipt, name='receipt'),
    path('payment/', payment, name='payment'),
]
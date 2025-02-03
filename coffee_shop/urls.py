from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', TemplateView.as_view(template_name="contact.html"), name='contact'),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('add-to-cart/<int:item_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', ViewCartView.as_view(), name='cart'),
    path('order/', OrderView.as_view(), name='order'),
    path('create-order/', CreateOrderView.as_view(), name='create_order'),
    path('mark-order-ready/<int:order_id>/', MarkOrderReadyView.as_view(), name='mark_order_ready'),
    path('receipt/<int:order_id>/', ReceiptView.as_view(), name='receipt'),
    path('payment/', TemplateView.as_view(template_name="payment.html"), name='payment'),
]
from django.shortcuts import render
from coffee_shop.models import Order

def cashier_dashboard(request):
    orders = Order.objects.filter(status='Pending')
    return render(request, 'cafe/dashboard.html', {'orders': orders})


def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'cafe/order_detail.html', {'order': order})

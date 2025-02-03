import json

from django.views import View
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from .models import *


class HomeView(ListView):
    model = MenuItem
    template_name = 'index.html'
    context_object_name = 'menu_items'

    def get_queryset(self):
        return MenuItem.objects.select_related('category').all()


class MenuView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'menu.html', {'categories': categories})


# افزودن آیتم به سبد خرید
cart = []
class AddToCartView(View):
    def get(self, request, item_id):
        item = get_object_or_404(MenuItem, id=item_id)
        cart = request.COOKIES.get('cart', '[]')
        cart = json.loads(cart)
        cart_item = {'id': item.id, 'name': item.name, 'price': item.price, 'quantity': 1}
        item_in_cart = next((i for i in cart if i['id'] == item.id), None)
        if item_in_cart:
            item_in_cart['quantity'] += 1
        else:
            cart.append(cart_item)
        response = redirect('menu')
        response.set_cookie('cart', json.dumps(cart), max_age=3600)  # Use json to serialize the cart list
        return response

# مشاهده سبد خرید
class ViewCartView(View):
    def get(self, request):
        cart = request.COOKIES.get('cart', '[]')
        cart = json.loads(cart)
        context = {'cart': cart}
        return render(request, 'cart.html', context)

# مشاهده سفارش‌ها
class OrderView(ListView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'order'


# ایجاد سفارش
class CreateOrderView(View):
    def get(self, request):
        order = Order.objects.create()
        for i in cart:
            order.menu_items.add(i)
        cart.clear()
        return render(request, 'order.html', {'order': Order.objects.prefetch_related('menu_items').all()})


# آماده‌سازی سفارش
class MarkOrderReadyView(View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        order.ready = True
        order.save()
        return redirect('order')


# صدور رسید
class ReceiptView(View):
    def get_context_data(self, **kwargs):
        context = {}
        # دریافت سفارش و رسید
        order = Order.objects.get(id=kwargs.get('order_id'))
        receipt = Receipt.objects.get(order=order)
        context['order'] = order
        context['receipt'] = receipt

        # می‌توانید داده‌های دیگر را به کانتکست اضافه کنید
        context['vat_amount'] = receipt.total_price * 0.1  # محاسبه مالیات
        context['final_price'] = receipt.total_price + context['vat_amount']
        return context

    def get(self, request, *args, **kwargs):
        """نمای GET"""
        context = self.get_context_data(**kwargs)
        return render(request, 'receipt.html', context)


    #
    # def get(self, request):
    #     vat = 0.10
    #     receipt = Receipt.objects.select_related('order').all()
    #     final_price = sum(i.order.menu_item.price * i.order.quantity for i in receipt)
    #     vat_amount = final_price * vat
    #     return render(request, 'receipt.html',
    #                   {'receipt': receipt, 'vat_amount': vat_amount, 'final_price': final_price})

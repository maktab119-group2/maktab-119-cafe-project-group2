import json
from datetime import timezone
from django.views import View
from django.views.generic import ListView, DetailView
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
        menu_items = MenuItem.objects.all()
        tables = Table.objects.all()

        table_number = request.GET.get('table_number', None)

        context = {
            "categories": categories,
            "menu_items": menu_items,
            "tables": tables,
            "table_number": table_number
        }
        return render(request, "menu.html", context)

cart = []
class AddToCartView(View):
    def get(self, request, item_id):
        item = get_object_or_404(MenuItem, id=item_id)
        cart = request.COOKIES.get('cart', '[]')
        cart = json.loads(cart)
        table_number = request.GET.get('table_number', None)

        cart_item = {
            'id': item.id,
            'name': item.name,
            'price': item.price,
            'quantity': 1,
            'discount': float(item.discount),
            'table_number': table_number
        }

        item_in_cart = next((i for i in cart if i['id'] == item.id), None)
        if item_in_cart:
            item_in_cart['quantity'] += 1  # Increase quantity if item already in the cart
        else:
            cart.append(cart_item)  # Otherwise, add new item to cart

        response = redirect('menu')  # Redirect to menu after adding the item
        response.set_cookie('cart', json.dumps(cart), max_age=3600)  # Store the updated cart in cookies
        return response


class ViewCartView(View):
    def get(self, request):
        cart = request.COOKIES.get('cart', '[]')
        cart = json.loads(cart)

        total_price = 0
        total_discount = 0
        final_price = 0

        # Calculate total price, discount, and final price
        for item in cart:
            item_price = item['price'] * item['quantity']
            item_discount = item['price'] * item['quantity'] * (item['discount'] / 100)
            total_price += item_price
            total_discount += item_discount

        final_price = total_price - total_discount

        context = {
            'cart': cart,
            'total_price': total_price,
            'total_discount': total_discount,
            'final_price': final_price,
        }

        return render(request, 'cart.html', context)


# مشاهده سفارش‌ها
class OrderView(ListView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'order'


# ایجاد سفارش
class CreateOrderView(View):
    def post(self, request):
        cart = request.COOKIES.get('cart', '[]')
        cart = json.loads(cart)

        # Create an order object
        table_number = request.GET.get('table_number', None)
        table = get_object_or_404(Table, table_number=table_number)

        # Create the Order
        order = Order.objects.create(table=table, timestamp=timezone.now())

        # Create OrderItems for each cart item
        for item in cart:
            menu_item = get_object_or_404(MenuItem, id=item['id'])
            order_item = OrderItem.objects.create(order=order, menu_item=menu_item, quantity=item['quantity'])

        # Create Receipt for the order
        receipt = Receipt.objects.create(order=order)

        # Optionally clear the cart after placing the order
        response = redirect('payment')  # Redirect to the payment page
        response.delete_cookie('cart')  # Remove the cart cookie after checkout
        return response


class PaymentView(View):
    def post(self, request):
        receipt_id = request.POST.get('receipt_id')
        amount = request.POST.get('amount')
        payment_method = request.POST.get('payment_method')

        receipt = get_object_or_404(Receipt, id=receipt_id)

        # Create Payment record
        Payment.objects.create(
            receipt=receipt,
            amount=amount,
            payment_method=payment_method,
        )

        # Optionally clear the cart or show success message
        response = redirect('payment_success')  # Redirect to success page
        return response


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


class TableListView(ListView):
    model = Table
    template_name = "TableList.html"  # مسیر قالب HTML
    context_object_name = "tables"  # نام متغیر ارسالی به قالب


class TableDetailView(DetailView):
    model = Table
    template_name = "TableDetail.html"
    context_object_name = "table"
    pk_url_kwarg = "table_id"  # برای گرفتن table_id از URL


from django.views import View

# def get(self, request):
#     vat = 0.10
#     receipt = Receipt.objects.select_related('order').all()
#     final_price = sum(i.order.menu_item.price * i.order.quantity for i in receipt)
#     vat_amount = final_price * vat
#     return render(request, 'receipt.html',
#                   {'receipt': receipt, 'vat_amount': vat_amount, 'final_price': final_price})

from pyexpat.errors import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import FormView, ListView
from cashier.forms import *
from coffee_shop.forms import *
from coffee_shop.models import *
from django.contrib import messages
from .managers import CustomUserManager


class AddMenuItemView(FormView):
    template_name = 'cafe/add_menu_item.html'
    form_class = MenuItemForm
    success_url = '/menu/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EditMenuItemView(View):
    def get(self, request, item_id):
        item = get_object_or_404(MenuItem, id=item_id)
        form = MenuItemForm(instance=item)
        return render(request, 'edit_menu_item.html', {'form': form})

    def post(self, request, item_id):
        item = get_object_or_404(MenuItem, id=item_id)
        form = MenuItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('menu')
        return render(request, 'edit_menu_item.html', {'form': form})


# class RegisterView(FormView):
#     template_name = 'register.html'
#     form_class = UserRegistrationForm
#     success_url = '/login/'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class LoginCashierView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login_cashier.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate user using email
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful! Welcome back.')
                return redirect('home')  # Redirect to home or another page after login
            else:
                form.add_error('email', 'Invalid email or password')
                messages.error(request, 'Invalid email or password. Please try again.')  # Error message
        return render(request, 'login.html', {'form': form})


class CashierDashboardView(ListView):
    model = Order
    template_name = 'cashier_dashboard.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(status='Pending')


class OrderDetailView(View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        return render(request, 'order_detail.html', {'order': order})


# class LoginCashierView(View):
#     def post(self, request):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('/admin/')
#         messages.error(request, 'Invalid username or password.')
#         return render(request, 'login.html')

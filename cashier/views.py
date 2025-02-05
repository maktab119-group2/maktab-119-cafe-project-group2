from pyexpat.errors import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import FormView, ListView, DetailView
from cashier.forms import *
from coffee_shop.forms import *
from coffee_shop.models import *
from django.contrib import messages
from django.views.generic import UpdateView
from django.urls import reverse_lazy


class ItemListView(ListView):
    model = MenuItem
    template_name = 'all_item.html'
    context_object_name = 'all_item'
    #
    # def get_queryset(self):
    #     queryset = MenuItem.objects.filter(is_deleted=False)
    #     # category_id = self.request.GET.get('category', 0)
    #     # if category_id:
    #     #     queryset = queryset.filter(category__id=category_id)
    #     return queryset

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['all_category'] = Category.objects.all()
    #     return context


class ItemDetailView(DetailView):
    model = MenuItem
    template_name = 'item_detail.html'
    context_object_name = 'item'

    def get_object(self):
        return get_object_or_404(MenuItem, id=self.kwargs['item_id'])


class AddMenuItemView(FormView):
    template_name = 'add_menu_item.html'
    form_class = MenuItemForm
    success_url = '/menu/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CashierEditMenuItemView(View):
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
                return redirect('cashier_dashboard')  # Redirect to home or another page after login
            else:
                form.add_error('email', 'Invalid email or password')
                messages.error(request, 'Invalid email or password. Please try again.')  # Error message
        return render(request, 'login_cashier.html', {'form': form})


class CashierOrdersListView(ListView):
    model = Order
    template_name = 'cashier_dashboard.html'
    context_object_name = 'orders'

    def get_queryset(self):
        orders = Order.objects.all()
        return orders

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_items'] = MenuItem.objects.all()  # اضافه کردن menu_items به context
        return context


class CashierOrderUpdateView(UpdateView):
    model = Order
    fields = ['ready']  # Cashier can update the "ready" status
    template_name = 'cashier/order_update.html'
    success_url = reverse_lazy('cashier_dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class TableListView(ListView):
    model = Table
    template_name = "TableList.html"  # مسیر قالب HTML
    context_object_name = "tables"  # نام متغیر ارسالی به قالب

class TableDetailView(DetailView):
    model = Table
    template_name = "TableDetail.html"
    context_object_name = "table"
class MarkOrderReadyView(View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        order.ready = True
        order.save()
        return redirect('cashier_dashboard')

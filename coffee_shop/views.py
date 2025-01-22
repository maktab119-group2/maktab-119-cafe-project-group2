from django.shortcuts import render, redirect
from .models import MenuItem, Category, Order, Receipt
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate, login
from .models import Order
from .forms import MenuItemForm

# Create your views here.
def home(request):
    categories = Category.objects.all()
    menu_items = MenuItem.objects.all()
    return render(request, 'index.html', {'menu_items': menu_items, 'categories': categories})


def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')


def menu(request):
    menu_items = MenuItem.objects.all()
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        if item_id:
            cart = request.session.get('cart', [])
            cart.append(item_id)
            request.session['cart'] = cart
            return redirect('menu')
    return render(request, 'menu.html', {'menu_items': menu_items})
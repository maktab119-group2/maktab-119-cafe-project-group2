from django.shortcuts import render, redirect
from .models import MenuItem, Category, Order, Receipt
from .forms import UserRegistrationForm, UserLoginForm, MenuItemForm
from django.contrib.auth import authenticate, login
from django.contrib import messages




# Create your views here.
def home(request):
    menu_items = MenuItem.objects.select_related('category').all()
    return render(request, 'index.html', {'menu_items': menu_items})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')


def menu(request):
    menu_items = MenuItem.objects.all()
    categories = Category.objects.prefetch_related('menuitem_set').all()
    category_id = request.GET.get('category_id')
    if category_id:
        menu_items = menu_items.filter(category_id=category_id)
    return render(request, 'menu.html', {'menu_items': menu_items, 'categories': categories})

cart = []
def add_to_cart(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    cart.append(item)
    return redirect('menu')

def view_cart(request):
    order = Order.objects.all()
    menu_items = Order.objects.select_related('menu_item').all()
    return render(request, 'cart.html', {'menu_items': menu_items, 'order': order, 'cart': cart})

def order_view(request):
    order = Order.objects.all()
    return render(request, 'order.html', {'order': order})

def create_order(request):
    order = Order.objects.create()
    for i in cart:
        order.menu_items.add(i)
    cart.clear()
    return render(request, 'order.html', {'order': Order.objects.prefetch_related('menu_items').all()})


def mark_order_ready(request, order_id):
    order = Order.objects.get(id=order_id)
    order.ready = True
    order.save()
    return redirect('order')

def receipt(request):
    context = {}
    vat = 0.10
    receipt = Receipt.objects.select_related('order').all()
    table = Order.objects.select_related('table').all()
    user = Order.objects.select_related('user').all()
    menu_item = Order.objects.prefetch_related('menu_item').all()
    order = Order.objects.all()
    final_price = 0
    for i in receipt:
        if i.order.menu_item.discount == 0:
            i.total_price = i.order.menu_item.price * i.order.quantity
        else:
            i.total_price =  i.order.quantity * (i.order.menu_item.price - (i.order.menu_item.price * (i.order.menu_item.discount/100)))
        final_price += i.total_price
        if not user.discount == 0:
            final_price -= final_price * user.discount
            messages = "Happy Birthday!"
        else:
            messages = "0"

        i.final_price = final_price
        i.save()

        vat_amount = final_price * vat

        context = {
            'receipt': receipt,
            'table': table,
            'user': user,
            'menu_item': menu_item,
            'order': order,
            'vat_amount': vat_amount,
            'final_price': final_price,
            'messages': messages
        }
    return render(request, 'receipt.html', context)


# def add_to_cart(request, item_id):
#     item = MenuItem.objects.get(id=item_id)
#     if request.method == 'POST':
#         item_id = request.POST.get(item)
#         if item_id:
#             cart = request.session.get('cart', {})
#             cart[item_id] = cart.get(item_id, 0) + 1
#             request.session['cart'] = cart
#             return render(request,'receipt.html', {'cart': cart})
#     return redirect('menu')

# def cart(request):
#     menu_items = MenuItem.objects.all()
#     cart = request.session.get('cart', [])
#
#     # Check if the product is already in the cart
#     product_exists = False
#     for item in cart:
#         if item['name'] == menu_items.name: # Compare by product name instead of ID
#             item['quantity'] += 1
#             product_exists = True
#             break
#
#     # If product is not in the cart, add it
#         if not product_exists:
#             cart.append({
#             'name': menu_items.name,
#             'price': menu_items.price,
#             'quantity': 1
#             })
#
#     # Save the cart back to the session
#     request.session['cart'] = cart
#     request.session.modified = True # Mark session as modified to ensure saving
#
#     return redirect('cart')

# def cart(request, menuitem_id):
#     response.set_cookie('menuitem_id', menuitem_id)
#     return request
#
# def set_session(request):
# 	request.session['username'] = 'mostafa'
# 	request.session['user_id'] = 12345
# 	request.session['is_logged_in'] = True
# 	return render(request, 'set_session.html')
#
# def get_session(request):
#     username = request.session.get('username', 'Guest')  # Default to 'Guest' if not set
#     is_logged_in = request.session.get('is_logged_in', False)
#     request.session.set_expiry(300)
#     return render(request, 'get_session.html', {'username': username, 'is_logged_in': is_logged_in})
#
# def view_cart(request):
#     response = request.COOKIES.get('menuitem_id', '')
#     return render(request, 'receipt.html', {'menuitem_id': response})

def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)  # Include request.FILES here
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = MenuItemForm()
    return render(request, 'cafe/add_menu_item.html', {'form': form})


def edit_menu_item(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=item)  # Include request.FILES here
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'cafe/edit_menu_item.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def cashier_dashboard(request):
    orders = Order.objects.filter(status='Pending')
    return render(request, 'cafe/dashboard.html', {'orders': orders})


def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'cafe/order_detail.html', {'order': order})



def payment(request):
    if request.method == 'POST':
        return redirect('menu')
    return render(request, 'payment.html')

def login_cashier(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/admin/')  # تغییر مسیر بعد از ورود موفق
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')
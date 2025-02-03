from django.urls import path
from .views import *

urlpatterns = [
    path('add-menu-item/', AddMenuItemView.as_view(), name='add_menu_item'),
    path('edit-menu-item/<int:item_id>/', EditMenuItemView.as_view(), name='edit_menu_item'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('cashier-dashboard/', CashierDashboardView.as_view(), name='cashier_dashboard'),
    path('order-detail/<int:order_id>/', OrderDetailView.as_view(), name='order_detail'),
    path('login-cashier/', LoginCashierView.as_view(), name='login_cashier'),
]
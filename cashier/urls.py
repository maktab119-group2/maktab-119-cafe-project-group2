from django.urls import path
from .views import *

urlpatterns = [
    path('all_item/', ItemListView.as_view(), name='all_item'),
    path('item_detail/<int:item_id>/', ItemDetailView.as_view(), name='item_detail'),
    path('add-menu-item/', AddMenuItemView.as_view(), name='add_menu_item'),
    path('edit-menu-item/<int:item_id>/', CashierEditMenuItemView.as_view(), name='edit_menu_item'),
    path('login/', LoginCashierView.as_view(), name='login_cashier'),
    path('cashier-dashboard/', CashierOrdersListView.as_view(), name='cashier_dashboard'),
    path('order/update/<int:pk>/', CashierOrderUpdateView.as_view(), name='order_update'),
    path('login-cashier/', LoginCashierView.as_view(), name='login_cashier'),

]
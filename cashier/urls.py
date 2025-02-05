from django.urls import path
from .views import *

urlpatterns = [
    path('all_item/', ItemListView.as_view(), name='all_item'),
    path('item_detail/<int:item_id>/', ItemDetailView.as_view(), name='item_detail'),
    path('add-menu-item/', AddMenuItemView.as_view(), name='add_menu_item'),
    path('edit-menu-item/<int:item_id>/', EditMenuItemView.as_view(), name='edit_menu_item'),
    # path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginCashierView.as_view(), name='login_cashier'),
    path('cashier-dashboard/', CashierDashboardView.as_view(), name='cashier_dashboard'),
    path('order-detail/<int:order_id>/', OrderDetailView.as_view(), name='order_detail'),
    path('login-cashier/', LoginCashierView.as_view(), name='login_cashier'),
    path("tables/", TableListView.as_view(), name="table_list"),
    path("tables/<int:table_id>/", TableDetailView.as_view(), name="table_detail"),

]
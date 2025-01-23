from django.contrib import admin
from coffee_shop.models import *


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount', 'payment_method', 'timestamp')



@admin.register(Receipt)    
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('order', 'total_price', 'final_price', 'timestamp')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "table", "status", "timestamp"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "menu_item", "quantity"]

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name' , 'price', 'category', 'discount', 'description', 'serving_time_period', 'estimated_cooking_time']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'email', 'password', 'birthday']

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'cafe_space_position']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


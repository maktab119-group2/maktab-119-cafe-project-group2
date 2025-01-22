from django.contrib import admin
from coffee_shop.models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "table", "menu_items", "status", "timestamp"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "menu_item", "timestamp"]

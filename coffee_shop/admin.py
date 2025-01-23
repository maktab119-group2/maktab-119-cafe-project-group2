from django.contrib import admin

from coffee_shop.models import *


# Register your models here.
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

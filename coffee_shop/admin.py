from django.contrib import admin

from coffee_shop.models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'email', 'password', 'birthday']

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'cafe_space_position']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

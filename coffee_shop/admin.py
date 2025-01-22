from django.contrib import admin

from coffee_shop.models import MenuItem


# Register your models here.
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name' , 'price', 'category', 'discount', 'description', 'serving_time_period', 'estimated_cooking_time']
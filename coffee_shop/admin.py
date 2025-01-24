from django.contrib import admin
from coffee_shop.models import Payment
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount', 'payment_method', 'timestamp')


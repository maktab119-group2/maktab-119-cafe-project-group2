from django.contrib import admin
from .models import Receipt


admin.site.register(Receipt)

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('order', 'total_price', 'final_price ', 'timestamp')
admin.site.register(Receipt, ReceiptAdmin)
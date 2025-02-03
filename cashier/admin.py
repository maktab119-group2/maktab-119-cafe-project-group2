from django.contrib.auth.admin import UserAdmin
from cashier.models import CashierUser, CustomUser
from django.contrib import admin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "is_superuser", "is_active")
    list_filter = ("is_superuser", "is_active")
    search_fields = ("email",)
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_superuser", "is_active", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff", "is_superuser", "is_active", "groups",
                "user_permissions"),
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request)


class CashierUserAdmin(UserAdmin):
    model = CashierUser
    list_display = ("email", "is_staff", "is_superuser")
    search_fields = ("email",)
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_superuser", "is_staff", "is_active", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff", "is_superuser", "is_active", "groups",
                "user_permissions"),
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_staff=True, is_superuser=False)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CashierUser, CashierUserAdmin)

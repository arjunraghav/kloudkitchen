from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "slug")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("User type"), {"fields": ("customer_type",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "username", "email", "password1", "password2", "customer_type"),
            },
        ),
    )
    list_display = ("username", "email", "first_name", "last_name", "customer_type")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    # fieldsets = (
    #     ('Group Permissions', {
    #         'fields': ('groups', 'user_permissions',)
    #     }),
    # )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomerProfile)
admin.site.register(VendorProfile)
admin.site.register(Testimonial)
admin.site.register(Review)
admin.site.register(Like)
admin.site.register(Following)
admin.site.register(Wallet)
admin.site.register(Coupon)

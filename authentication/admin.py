from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Information",
            {
                "fields": (
                    "phone",
                    "role",
                )
            }
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional Information",
            {
                "fields": (
                    "email",
                    "phone",
                    "role",
                )
            }
        ),
    )

    list_display = (
        "email",
        "username",
        "role",
        "phone",
        "is_active",
    )

    list_filter = (
        "role",
        "is_active",
    )

    search_fields = (
        "email",
        "username",
    )
from django.contrib import admin
from .models import Restaurant, Table


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "phone",
        "created_at",
    )


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "restaurant",
        "seats",
        "status",
    )

    list_filter = (
        "status",
        "restaurant",
    )
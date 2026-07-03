from django.contrib import admin
from apps.website.models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "location",
        "parent",
        "display_order",
        "is_active",
    )

    list_filter = (
        "location",
        "is_active",
    )

    search_fields = (
        "title",
        "url",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    ordering = (
        "location",
        "display_order",
    )

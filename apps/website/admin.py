from django.contrib import admin
from apps.website.models import MenuItem
from apps.website.models import Page


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


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "featured",
        "published_at",
    )

    list_filter = (
        "status",
        "featured",
    )

    search_fields = (
        "title",
        "summary",
        "content",
    )

    prepopulated_fields = {"slug": ("title",)}

    list_editable = (
        "status",
        "featured",
    )

    ordering = ("-published_at",)

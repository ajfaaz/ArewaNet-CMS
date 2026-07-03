from django.contrib import admin

from apps.pages.models import Page


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

from django.contrib import admin
from django.utils.html import format_html
from apps.content.registry import registry
from apps.content.models import PageComponent


@admin.register(PageComponent)
class PageComponentAdmin(admin.ModelAdmin):

    list_display = (
        "page",
        "component_type",
        "heading",
        "display_order",
        "status",
        "is_active",
        "image_preview",
    )

    list_filter = (
        "component_type",
        "page",
        "status",
        "is_active",
    )

    search_fields = (
        "heading",
        "subheading",
        "body",
    )

    ordering = (
        "page",
        "display_order",
    )

    list_editable = (
        "display_order",
        "status",
        "is_active",
    )

    readonly_fields = ("image_preview",)

    def get_fieldsets(self, request, obj=None):

        component = None

        if obj:
            component = obj.component_type

        base = [
            (
                "General",
                {
                    "fields": (
                        "page",
                        "component_type",
                        "status",
                        "published_at",
                        "display_order",
                        "is_active",
                    )
                },
            )
        ]

        if component == "hero":

            base += [
                (
                    "Hero Content",
                    {
                        "fields": (
                            "heading",
                            "subheading",
                            "body",
                        )
                    },
                ),
                (
                    "Buttons",
                    {
                        "fields": (
                            "button_text",
                            "button_url",
                            "secondary_button_text",
                            "secondary_button_url",
                        )
                    },
                ),
                (
                    "Hero Image",
                    {
                        "fields": (
                            "background_image",
                            "image",
                            "image_preview",
                        )
                    },
                ),
                (
                    "Appearance",
                    {
                        "fields": (
                            "text_alignment",
                            "hero_height",
                            "overlay_color",
                            "overlay_opacity",
                            "enable_animation",
                        )
                    },
                ),
            ]

        elif component == "rich_text":

            base += [
                (
                    "Content",
                    {
                        "fields": (
                            "heading",
                            "body",
                        )
                    },
                ),
            ]

        elif component == "image":

            base += [
                (
                    "Image",
                    {
                        "fields": (
                            "heading",
                            "image",
                            "image_preview",
                        )
                    },
                ),
            ]

        else:

            base += [
                (
                    "Content",
                    {
                        "fields": (
                            "heading",
                            "subheading",
                            "body",
                            "image",
                            "image_preview",
                        )
                    },
                ),
            ]

        base += [
            (
                "Advanced",
                {
                    "classes": ("collapse",),
                    "fields": ("configuration",),
                },
            )
        ]

        return base

    def image_preview(self, obj):

        if obj.background_image:

            return format_html(
                '<img src="{}" style="height:80px;border-radius:8px;">',
                obj.background_image.url,
            )

        if obj.image:

            return format_html(
                '<img src="{}" style="height:80px;border-radius:8px;">',
                obj.image.url,
            )

        return "-"

    image_preview.short_description = "Preview"

    def get_form(self, request, obj=None, **kwargs):

        if obj:

            form_class = registry.get_form(obj.component_type)

            if form_class:
                kwargs["form"] = form_class

        return super().get_form(
            request,
            obj,
            **kwargs,
        )

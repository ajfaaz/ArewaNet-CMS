from django.contrib import admin
from apps.core.models import WebsiteSettings


@admin.register(WebsiteSettings)
class WebsiteSettingsAdmin(admin.ModelAdmin):
    list_display = (
        "organization_name",
        "email",
        "phone",
    )

    fieldsets = (
        (
            "Organization",
            {
                "fields": (
                    "organization_name",
                    "short_name",
                    "logo",
                    "favicon",
                )
            },
        ),
        (
            "Contact",
            {
                "fields": (
                    "email",
                    "phone",
                    "phone_two",
                    "address",
                )
            },
        ),
        (
            "Social Media",
            {
                "fields": (
                    "facebook",
                    "instagram",
                    "twitter",
                    "tiktok",
                    "youtube",
                    "whatsapp",
                )
            },
        ),
        (
            "Branding",
            {
                "fields": (
                    "primary_color",
                    "secondary_color",
                    "footer_text",
                )
            },
        ),
        (
            "About",
            {
                "fields": (
                    "mission",
                    "vision",
                )
            },
        ),
    )

    def has_add_permission(self, request):
        # Prevents creating more than one settings instance in the admin panel
        return not WebsiteSettings.objects.exists()

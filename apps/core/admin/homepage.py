from django.contrib import admin
from apps.core.models import (
    WebsiteSettings,
    HeroSlide,
    Statistic,
    AboutSection,
)


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "display_order",
        "is_active",
    )

    list_editable = (
        "display_order",
        "is_active",
    )

    search_fields = ("title",)


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "value",
        "display_order",
        "is_active",
    )

    list_editable = (
        "display_order",
        "is_active",
    )


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "is_active",
    )

    list_editable = ("is_active",)

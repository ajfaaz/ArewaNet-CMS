from .models import (
    WebsiteSettings,
    HeroSlide,
    Statistic,
    AboutSection,
)


def website_settings(request):

    website = WebsiteSettings.objects.first()

    hero_slides = HeroSlide.objects.filter(is_active=True)

    statistics = Statistic.objects.filter(is_active=True)

    about = AboutSection.objects.filter(is_active=True).first()

    return {
        "website": website,
        "hero_slides": hero_slides,
        "statistics": statistics,
        "homepage_about": about,
    }

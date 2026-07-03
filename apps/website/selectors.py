from apps.website.models import Page


def get_published_pages():
    return Page.objects.filter(
        status="published",
        is_active=True,
    ).order_by(
        "display_order",
        "title",
    )


def get_page_by_slug(slug):
    return Page.objects.get(
        slug=slug,
        status="published",
        is_active=True,
    )

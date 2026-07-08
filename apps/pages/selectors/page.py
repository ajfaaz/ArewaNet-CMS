from django.shortcuts import get_object_or_404

from apps.pages.models import Page


def get_page(slug):

    return get_object_or_404(
        Page.objects.prefetch_related("components"),
        slug=slug,
        status="published",
    )

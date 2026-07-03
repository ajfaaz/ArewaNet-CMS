from django.shortcuts import get_object_or_404, render
from apps.pages.models import Page


def page_detail(request, slug):
    page = get_object_or_404(
        Page,
        slug=slug,
        status="published",
    )

    return render(
        request,
        "website/page_detail.html",
        {
            "page": page,
        },
    )

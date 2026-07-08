from django.shortcuts import get_object_or_404
from django.shortcuts import render

from apps.pages.models import Page


def page_builder(request, pk):

    page = get_object_or_404(
        Page,
        pk=pk,
    )

    return render(
        request,
        "builder/editor.html",
        {
            "page": page,
        },
    )

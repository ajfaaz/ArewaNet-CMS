from django.shortcuts import render

from apps.pages.selectors import get_page

from apps.content.services import render_components


def page_detail(request, slug):

    page = get_page(slug)

    rendered_components = render_components(page)

    return render(
        request,
        "pages/page.html",
        {
            "page": page,
            "components": rendered_components,
        },
    )

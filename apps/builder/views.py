import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST

from apps.content.models import PageComponent
from apps.pages.models import Page


def page_builder(request, pk):
    page = get_object_or_404(
        Page,
        pk=pk,
    )

    components = PageComponent.objects.filter(page=page).order_by("display_order")

    return render(
        request,
        "builder/editor.html",
        {
            "page": page,
            "components": components,
        },
    )


def dashboard(request):
    pages = Page.objects.all().order_by("title")

    return render(
        request,
        "builder/dashboard.html",
        {
            "pages": pages,
        },
    )


@require_POST
def update_component(request, pk):
    """
    Asynchronously update an individual PageComponent's content values.
    Currently optimized for layout mutations targeting the Hero variant.
    """
    component = get_object_or_404(PageComponent, pk=pk)

    try:
        # Load JSON dataset payload from request body
        data = json.loads(request.body)

        # Map client parameters to Hero model properties safely using fallbacks
        if "heading" in data:
            component.heading = data.get("heading")
        if "subheading" in data:
            component.subheading = data.get("subheading")
        if "button_text" in data:
            component.button_text = data.get("button_text")

        component.save()

        return JsonResponse({"success": True})

    except (json.JSONDecodeError, KeyError) as error:
        return JsonResponse(
            {"success": False, "error": f"Invalid format package: {str(error)}"},
            status=400,
        )
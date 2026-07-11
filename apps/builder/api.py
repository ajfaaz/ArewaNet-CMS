from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from apps.content.models import PageComponent


def component_detail(request, pk):
    component = get_object_or_404(PageComponent, pk=pk)

    return JsonResponse({
        "id": component.id,
        "type": component.component_type,
        "heading": component.heading,
        "subheading": component.subheading,
        "button_text": component.button_text,
        "button_url": component.button_url,
        "alignment": component.text_alignment,
    })
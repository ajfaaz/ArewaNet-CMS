from django.shortcuts import render

from apps.cms.services.dashboard import get_dashboard_widgets


def dashboard(request):

    return render(
        request,
        "cms/dashboard.html",
        {
            "widgets": get_dashboard_widgets(request.user),
        },
    )
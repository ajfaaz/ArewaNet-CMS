from django.shortcuts import render


def menu_list(request):
    return render(
        request,
        "website/cms/menu_list.html",
    )

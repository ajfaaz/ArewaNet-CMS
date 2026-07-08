from django.shortcuts import render


def page_list(request):

    return render(
        request,
        "pages/cms/page_list.html",
    )

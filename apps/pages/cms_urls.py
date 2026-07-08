from django.urls import path

from .cms_views import page_list

urlpatterns = [
    path(
        "",
        page_list,
        name="cms_pages",
    ),
]

from django.urls import path

from apps.website.views import page_detail

urlpatterns = [
    path(
        "pages/<slug:slug>/",
        page_detail,
        name="page_detail",
    ),
]

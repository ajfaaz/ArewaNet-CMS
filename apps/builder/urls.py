from django.urls import path

from .views import page_builder

urlpatterns = [
    path(
        "page/<int:pk>/",
        page_builder,
        name="page_builder",
    ),
]

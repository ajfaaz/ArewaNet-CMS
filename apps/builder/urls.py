from django.urls import path
from . import views
from .api import component_detail

app_name = "builder"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    path(
        "page/<int:pk>/",
        views.page_builder,
        name="page_builder",
    ),

    path(
        "api/component/<int:pk>/",
        component_detail,
        name="component_detail",
    ),

    path(
        "component/<int:pk>/update/",
        views.update_component,
        name="update_component",
    ),
]

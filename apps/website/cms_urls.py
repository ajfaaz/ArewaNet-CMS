from django.urls import path

from .cms_views import menu_list

urlpatterns = [
    path(
        "",
        menu_list,
        name="cms_menus",
    ),
]

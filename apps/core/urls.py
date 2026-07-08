from django.urls import path
from . import views
from apps.pages.views.page import page_detail

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    # Always last
    path("<slug:slug>/", page_detail, name="page_detail"),
]

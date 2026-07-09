from django.urls import path
from . import views

app_name = "builder"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("page/<int:pk>/", views.page_builder, name="page_builder"),
]
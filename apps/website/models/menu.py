from django.db import models
from apps.core.models.base import OrderedModel
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class MenuItem(OrderedModel):
    LOCATION_CHOICES = (
        ("header", "Header"),
        ("footer", "Footer"),
        ("mobile", "Mobile"),
    )

    LINK_TYPE_CHOICES = (
        ("internal", "Internal"),
        ("external", "External"),
    )

    title = models.CharField(max_length=100)

    description = models.CharField(
        max_length=200,
        blank=True,
    )

    url = models.CharField(
        max_length=255,
        help_text="Example: /about/ or https://example.com",
    )

    link_type = models.CharField(
        max_length=20,
        choices=LINK_TYPE_CHOICES,
        default="internal",
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )

    location = models.CharField(
        max_length=20,
        choices=LOCATION_CHOICES,
        default="header",
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: fa-solid fa-house",
    )

    css_class = models.CharField(
        max_length=100,
        blank=True,
    )

    open_in_new_tab = models.BooleanField(default=False)

    class Meta:
        ordering = ("location", "display_order")

    def __str__(self):
        return f"{self.title} ({self.location})"

    @property
    def has_children(self):
        return self.children.filter(is_active=True).exists()

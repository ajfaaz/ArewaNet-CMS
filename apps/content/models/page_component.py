from django.db import models

from apps.core.models.base import OrderedModel
from apps.pages.models import Page


class PageComponent(OrderedModel):

    COMPONENT_TYPES = (
        ("hero", "Hero"),
        ("rich_text", "Rich Text"),
        ("image", "Image"),
        ("gallery", "Gallery"),
        ("statistics", "Statistics"),
        ("cta", "Call To Action"),
        ("faq", "FAQ"),
        ("team", "Team"),
        ("partners", "Partners"),
        ("video", "Video"),
        ("contact_form", "Contact Form"),
        ("donation", "Donation"),
        ("custom_html", "Custom HTML"),
    )

    TEXT_ALIGNMENT = (
        ("start", "Left"),
        ("center", "Center"),
        ("end", "Right"),
    )

    HERO_HEIGHT = (
        ("small", "Small (400px)"),
        ("medium", "Medium (600px)"),
        ("large", "Large (800px)"),
        ("fullscreen", "Full Screen"),
    )

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    # =====================================================
    # General
    # =====================================================

    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        related_name="components",
    )

    component_type = models.CharField(
        max_length=30,
        choices=COMPONENT_TYPES,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="published",
    )

    published_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    # =====================================================
    # Content
    # =====================================================

    heading = models.CharField(
        max_length=255,
        blank=True,
    )

    subheading = models.CharField(
        max_length=255,
        blank=True,
    )

    body = models.TextField(
        blank=True,
    )

    # =====================================================
    # Buttons
    # =====================================================

    button_text = models.CharField(
        max_length=100,
        blank=True,
    )

    button_url = models.CharField(
        max_length=255,
        blank=True,
    )

    secondary_button_text = models.CharField(
        max_length=100,
        blank=True,
    )

    secondary_button_url = models.CharField(
        max_length=255,
        blank=True,
    )

    # =====================================================
    # Images
    # =====================================================

    image = models.ImageField(
        upload_to="components/",
        blank=True,
        null=True,
    )

    background_image = models.ImageField(
        upload_to="components/backgrounds/",
        blank=True,
        null=True,
    )

    # =====================================================
    # Hero Settings
    # =====================================================

    text_alignment = models.CharField(
        max_length=20,
        choices=TEXT_ALIGNMENT,
        default="center",
    )

    hero_height = models.CharField(
        max_length=20,
        choices=HERO_HEIGHT,
        default="large",
    )

    overlay_color = models.CharField(
        max_length=20,
        default="#000000",
    )

    overlay_opacity = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.50,
    )

    enable_animation = models.BooleanField(
        default=True,
    )

    # =====================================================
    # Extra Configuration
    # =====================================================

    configuration = models.JSONField(
        default=dict,
        blank=True,
    )

    class Meta:
        ordering = ("display_order",)

    def __str__(self):
        return f"{self.page.title} • {self.get_component_type_display()}"

    # =====================================================
    # Configuration Helpers
    # =====================================================

    def get_config(self, key, default=None):
        """
        Return a configuration value.
        """

        return self.configuration.get(key, default)

    def set_config(self, key, value):
        """
        Save a configuration value.
        """

        self.configuration[key] = value

    def remove_config(self, key):
        """
        Remove a configuration value.
        """

        self.configuration.pop(key, None)

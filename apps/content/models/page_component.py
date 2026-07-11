from django.db import models
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe

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

    @property
    def preview(self):
        if self.component_type == "hero":
            heading = escape(self.heading or "Hero Preview")
            subheading = escape(self.subheading or "Building something great")
            button_text = escape(self.button_text or "Learn More")
            button_url = escape(self.button_url or "#")

            return mark_safe(
                format_html(
                    """
                    <div class="hero-preview">
                        <h2 class="hero-heading">{}</h2>
                        <p class="hero-subheading">{}</p>
                        <a class="hero-button" href="{}">{}</a>
                    </div>
                    """,
                    heading,
                    subheading,
                    button_url,
                    button_text,
                )
            )

        title = self.heading or f"{self.get_component_type_display()} Preview"
        subtitle = self.subheading or ""
        body = self.body or ""

        parts = [format_html("<h3>{}</h3>", escape(title))]

        if subtitle:
            parts.append(format_html("<p>{}</p>", escape(subtitle)))

        if body:
            parts.append(format_html("<div>{}</div>", escape(body[:160])))

        return mark_safe("".join(str(part) for part in parts))

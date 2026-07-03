from django.db import models
from .base import TimeStampedModel


class WebsiteSettings(models.Model):
    organization_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50, default="IASON")

    logo = models.ImageField(upload_to="settings/", blank=True, null=True)
    favicon = models.ImageField(upload_to="settings/", blank=True, null=True)

    email = models.EmailField(blank=True)

    phone = models.CharField(max_length=30, blank=True)

    phone_two = models.CharField(max_length=30, blank=True)

    address = models.TextField(blank=True)

    facebook = models.URLField(blank=True)

    instagram = models.URLField(blank=True)

    twitter = models.URLField(blank=True)

    tiktok = models.URLField(blank=True)

    youtube = models.URLField(blank=True)

    whatsapp = models.CharField(max_length=30, blank=True)

    primary_color = models.CharField(max_length=7, default="#0F766E")

    secondary_color = models.CharField(max_length=7, default="#F59E0B")

    footer_text = models.CharField(
        max_length=255, default="Powered by ArewaNet Ventures"
    )

    mission = models.TextField(blank=True)

    vision = models.TextField(blank=True)

    class Meta:
        verbose_name = "Website Settings"
        verbose_name_plural = "Website Settings"

    def __str__(self):
        return self.organization_name

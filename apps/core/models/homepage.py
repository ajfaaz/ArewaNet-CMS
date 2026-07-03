from django.db import models
from .base import OrderedModel


class HeroSlide(models.Model):
    title = models.CharField(max_length=200)

    subtitle = models.TextField()

    background_image = models.ImageField(upload_to="heroes/")

    button_one_text = models.CharField(max_length=50, default="Donate Now")

    button_one_url = models.CharField(max_length=255, default="/donate/")

    button_two_text = models.CharField(max_length=50, blank=True)

    button_two_url = models.CharField(max_length=255, blank=True)

    display_order = models.PositiveIntegerField(default=1)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.title


class Statistic(models.Model):
    title = models.CharField(max_length=100)

    value = models.PositiveIntegerField()

    icon = models.CharField(max_length=50, help_text="FontAwesome class e.g. fa-users")

    display_order = models.PositiveIntegerField(default=1)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["display_order"]

    def __str__(self):
        return self.title


class AboutSection(models.Model):
    title = models.CharField(max_length=200)

    subtitle = models.CharField(max_length=300, blank=True)

    content = models.TextField()

    image = models.ImageField(upload_to="about/", blank=True, null=True)

    button_text = models.CharField(max_length=50, default="Learn More")

    button_url = models.CharField(max_length=255, default="/about/")

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Homepage About Section"
        verbose_name_plural = "Homepage About Section"

    def __str__(self):
        return self.title

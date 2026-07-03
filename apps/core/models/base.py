from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class TimeStampedModel(models.Model):
    """
    Automatically tracks creation and modification dates.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PublishableModel(TimeStampedModel):
    """
    Adds publishing workflow.
    """

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft",
    )

    published_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.status == "published" and self.published_at is None:
            self.published_at = timezone.now()

        super().save(*args, **kwargs)


class OrderedModel(PublishableModel):
    """
    Adds ordering support.
    """

    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        abstract = True


class SlugModel(models.Model):
    """
    Automatically generates slugs from title.
    """

    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
    )

    class Meta:
        abstract = True

    def generate_slug(self):
        if hasattr(self, "title") and self.title:
            self.slug = slugify(self.title)


class SEOModel(models.Model):
    """
    Reusable SEO fields.
    """

    meta_title = models.CharField(
        max_length=255,
        blank=True,
    )

    meta_description = models.TextField(
        blank=True,
    )

    meta_keywords = models.CharField(
        max_length=500,
        blank=True,
    )

    class Meta:
        abstract = True

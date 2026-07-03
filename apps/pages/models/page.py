from django.db import models

from apps.core.models.base import (
    OrderedModel,
    SlugModel,
    SEOModel,
)


class Page(
    OrderedModel,
    SlugModel,
    SEOModel,
):
    title = models.CharField(max_length=200)

    summary = models.TextField(blank=True)

    content = models.TextField()

    featured_image = models.ImageField(
        upload_to="pages/",
        blank=True,
        null=True,
    )

    featured = models.BooleanField(default=False)

    class Meta:
        ordering = [
            "display_order",
            "title",
        ]

    def save(self, *args, **kwargs):
        self.generate_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

from django.db import models

from .base import OrderedModel, SlugModel, SEOModel


class ContentModel(
    OrderedModel,
    SlugModel,
    SEOModel,
):
    """
    Base class for all CMS content.
    """

    title = models.CharField(
        max_length=200,
    )

    summary = models.TextField(
        blank=True,
    )

    featured_image = models.ImageField(
        upload_to="content/",
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True

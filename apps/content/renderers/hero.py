from .base import BaseRenderer
from .registry import register


@register("hero")
class HeroRenderer(BaseRenderer):

    template_name = "content/components/hero.html"

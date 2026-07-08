from .base import BaseRenderer
from .registry import register


@register("rich_text")
class RichTextRenderer(BaseRenderer):

    template_name = "content/components/rich_text.html"

from django.template.loader import render_to_string
from django.template import TemplateDoesNotExist


class ComponentRenderer:

    @staticmethod
    def preview_template(component):
        return f"content/preview/{component.component_type}.html"

    @classmethod
    def render_preview(cls, component):

        try:

            return render_to_string(
                cls.preview_template(component),
                {
                    "component": component,
                },
            )

        except TemplateDoesNotExist:

            return render_to_string(
                "content/preview/default.html",
                {
                    "component": component,
                },
            )

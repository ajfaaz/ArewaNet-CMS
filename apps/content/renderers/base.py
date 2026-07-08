from django.template.loader import render_to_string

from apps.content.services.configuration import ComponentConfiguration


class BaseRenderer:

    template_name = None

    def render(self, component):

        config = ComponentConfiguration(component)

        return render_to_string(
            self.template_name,
            {
                "component": component,
                "config": config,
            },
        )

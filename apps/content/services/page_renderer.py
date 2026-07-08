from apps.content.registry import registry


def render_components(page):

    rendered = []

    for component in page.components.filter(
        is_active=True,
        status="published",
    ):

        renderer_class = registry.get_renderer(component.component_type)

        if renderer_class:

            renderer = renderer_class()

            rendered.append(renderer.render(component))

    return rendered

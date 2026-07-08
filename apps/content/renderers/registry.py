RENDERERS = {}


def register(component_type):

    def decorator(renderer):

        RENDERERS[component_type] = renderer

        return renderer

    return decorator


def get_renderer(component_type):

    return RENDERERS.get(component_type)

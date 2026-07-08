class ComponentRegistry:

    def __init__(self):
        self._components = {}

    def register(
        self,
        component_type,
        renderer=None,
        form=None,
        template=None,
        icon=None,
        name=None,
    ):
        self._components[component_type] = {
            "renderer": renderer,
            "form": form,
            "template": template,
            "icon": icon,
            "name": name,
        }

    def get(self, component_type):
        return self._components.get(component_type)

    def get_renderer(self, component_type):
        component = self.get(component_type)
        if component:
            return component["renderer"]

    def get_form(self, component_type):
        component = self.get(component_type)
        if component:
            return component["form"]

    def get_template(self, component_type):
        component = self.get(component_type)
        if component:
            return component["template"]

    def all(self):
        return self._components


registry = ComponentRegistry()
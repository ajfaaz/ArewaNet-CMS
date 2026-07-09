from apps.cms.registry.registry import registry
from apps.cms.registry.widgets import widgets


class CMSKernel:

    def __init__(self):
        self._plugins = []

    @property
    def modules(self):
        return registry

    @property
    def widgets(self):
        return widgets

    @property
    def plugins(self):
        return self._plugins

    def register_plugin(self, plugin):
        self._plugins.append(plugin)

        self.modules.register(plugin.module)

        for widget in plugin.widgets:
            self.widgets.register(widget)


kernel = CMSKernel()
from apps.cms.registry.registry import registry
from apps.cms.registry.widgets import widgets


class CMSKernel:

    @property
    def modules(self):
        return registry

    @property
    def widgets(self):
        return widgets


kernel = CMSKernel()
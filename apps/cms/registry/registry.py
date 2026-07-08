from collections import defaultdict

from .module import CMSModule


class CMSModuleRegistry:

    def __init__(self):
        self._modules = []

    # -------------------------------------
    # Registration
    # -------------------------------------

    def register(self, module: CMSModule):

        self._validate(module)

        self._modules.append(module)

        self._sort()

    # -------------------------------------
    # Validation
    # -------------------------------------

    def _validate(self, module):

        if not module.name:
            raise ValueError("Module name cannot be empty.")

        if not module.url_name:
            raise ValueError(f"{module.name}: url_name is required.")

        for existing in self._modules:

            if existing.name == module.name:
                raise ValueError(f"Duplicate module name: {module.name}")

            if existing.url_name == module.url_name:
                raise ValueError(f"Duplicate url_name: {module.url_name}")

    # -------------------------------------
    # Sorting
    # -------------------------------------

    def _sort(self):

        self._modules.sort(
            key=lambda m: (
                m.category,
                m.order,
                m.name,
            )
        )

    # -------------------------------------
    # Public APIs
    # -------------------------------------

    def all(self):
        return list(self._modules)

    def enabled(self):

        return [m for m in self._modules if m.enabled]

    def dashboard_modules(self):
        """
        Compatibility helper.

        Returns all dashboard widgets contributed
        by enabled CMS modules.
        """
        from .widgets import widgets as widget_registry

        return widget_registry.all()

    def categories(self):

        categories = defaultdict(list)

        for module in self.enabled():
            categories[module.category].append(module)

        return dict(categories)

    def get(self, name):

        for module in self._modules:

            if module.name == name:
                return module

        return None


# -------------------------------------------------
# Global Registry Instance
# -------------------------------------------------

registry = CMSModuleRegistry()

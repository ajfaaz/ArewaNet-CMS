from .widget import CMSWidget


class WidgetRegistry:

    def __init__(self):
        self._widgets = []

    def register(self, widget: CMSWidget):
        self._widgets.append(widget)
        self._widgets.sort(key=lambda w: w.order)

    def all(self):
        return list(self._widgets)

    def enabled(self, user=None):

        widgets = []

        for widget in self._widgets:

            if widget.permission and user:

                if not user.has_perm(widget.permission):
                    continue

            widgets.append(widget)

        return widgets


widgets = WidgetRegistry()
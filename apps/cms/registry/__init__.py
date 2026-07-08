from .module import CMSModule
from .registry import registry
from .widget import CMSWidget
from .widgets import widgets


def register_module(**kwargs):
    payload = dict(kwargs)

    if "url" in payload and "url_name" not in payload:
        payload["url_name"] = payload.pop("url")

    registry.register(CMSModule(**payload))


def register_widget(**kwargs):
    widgets.register(CMSWidget(**kwargs))
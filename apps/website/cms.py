from apps.cms.registry import register_module

register_module(
    name="Menus",
    icon="bi bi-list",
    url_name="cms_menus",
    permission=None,
    order=30,
)

from apps.cms.kernel import kernel
from apps.cms.plugin import CMSPlugin
from apps.cms.registry.module import CMSModule


website_plugin = CMSPlugin(
    module=CMSModule(
        name="Menus",
        icon="bi bi-list",
        url_name="cms_menus",
        permission=None,
        category="Website",
        description="Manage navigation menus",
        order=30,
    ),
)

kernel.register_plugin(website_plugin)
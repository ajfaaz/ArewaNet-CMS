from apps.cms.kernel import kernel
from apps.cms.plugin import CMSPlugin
from apps.cms.registry.module import CMSModule

builder_plugin = CMSPlugin(
    module=CMSModule(
        name="Builder",
        url_name="builder:dashboard",
        icon="bi-columns-gap",
        category="Website",
        permission="builder.view_builder",
        description="Visual page builder",
        order=10,
    ),
)

kernel.register_plugin(builder_plugin)
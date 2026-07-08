from apps.cms.registry import register_module


register_module(
    name="Builder",
    url_name="builder:dashboard",
    icon="bi-columns-gap",
    category="Website",
    permission="builder.view_builder",
    description="Visual page builder",
    order=10,
)

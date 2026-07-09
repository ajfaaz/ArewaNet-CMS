from apps.cms.plugin import CMSPlugin
from apps.cms.registry.module import CMSModule
from apps.cms.registry.widget import CMSWidget
from apps.cms.kernel import kernel

# Step 2 — Create the module object
pages_module = CMSModule(
    name="Pages",
    icon="bi bi-file-earmark",
    url_name="cms_pages",
    category="Website",
    permission=None,
    description="Manage website pages",
    order=20,
)

# Step 3 — Create the widget object
pages_widget = CMSWidget(
    title="Pages",
    template="pages/cms/widgets/pages_count.html",
    order=10,
)

# Step 4 — Create the plugin enclosing both resources
pages_plugin = CMSPlugin(
    module=pages_module,
    widgets=[
        pages_widget,
    ],
)

# Step 5 — Register the single consolidated plugin configuration
kernel.register_plugin(pages_plugin)
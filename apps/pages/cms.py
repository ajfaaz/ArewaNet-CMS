from apps.cms.registry import register_module
from apps.cms.registry import register_widget

register_widget(
    title="Pages",
    template="pages/cms/widgets/pages_count.html",
    order=10,
)

register_module(
    name="Pages",
    icon="bi bi-file-earmark-text",
    url_name="cms_pages",
    permission=None,
    order=20,
)

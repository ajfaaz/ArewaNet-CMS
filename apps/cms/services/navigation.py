from django.urls import NoReverseMatch, reverse
from apps.cms.kernel import kernel


def _resolve_module_url(module):
    try:
        return reverse(module.url_name)
    except NoReverseMatch:
        return None


def get_sidebar_modules():
    """
    Returns enabled CMS modules grouped by category with rich metadata.
    """
    categories = kernel.modules.categories()
    result = {}
    for category, modules in categories.items():
        result[category] = [
            {
                "title": module.name,
                "description": module.description,
                "icon": module.icon,
                "url_name": module.url_name,
                "url": _resolve_module_url(module),
                "badge": module.badge_callback() if module.badge_callback else None,
            }
            for module in modules
        ]
    return result

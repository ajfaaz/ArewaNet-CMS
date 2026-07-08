from apps.cms.services.navigation import get_sidebar_modules


def cms_navigation(request):
    return {
        "cms_sidebar": get_sidebar_modules(),
    }

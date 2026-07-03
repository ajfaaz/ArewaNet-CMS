from apps.website.services import MenuService


def menu_context(request):
    return {
        "header_menu": MenuService.header_menu(),
        "footer_menu": MenuService.footer_menu(),
    }

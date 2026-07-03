from apps.website.models import MenuItem


class MenuService:
    @staticmethod
    def header_menu():
        return (
            MenuItem.objects.filter(
                location="header",
                is_active=True,
                parent__isnull=True,
            )
            .prefetch_related("children")
            .order_by("display_order")
        )

    @staticmethod
    def footer_menu():
        return (
            MenuItem.objects.filter(
                location="footer",
                is_active=True,
                parent__isnull=True,
            )
            .prefetch_related("children")
            .order_by("display_order")
        )

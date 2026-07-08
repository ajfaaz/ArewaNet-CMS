from django.test import SimpleTestCase

from apps.cms.kernel import kernel
from apps.cms.registry import register_module
from apps.cms.registry import register_widget
from apps.cms.registry.registry import registry


class CMSRegistryTests(SimpleTestCase):
    def test_register_module_accepts_url_alias_and_description(self):
        original_modules = registry._modules
        registry._modules = []

        try:
            register_module(
                name="Menus",
                icon="bi bi-list",
                url="cms_menus",
                description="Main navigation",
                permission=None,
                order=10,
            )

            module = kernel.modules.all()[-1]
            self.assertEqual(module.url_name, "cms_menus")
            self.assertEqual(module.description, "Main navigation")
        finally:
            registry._modules = original_modules

    def test_grouped_aliases_by_category(self):
        original_modules = registry._modules
        registry._modules = []

        try:
            register_module(
                name="Builder",
                icon="bi-columns-gap",
                url_name="builder:dashboard",
                category="Website",
                order=10,
            )
            register_module(
                name="Reports",
                icon="bi-graph-up",
                url_name="reports:dashboard",
                category="Analytics",
                order=20,
            )

            categories_data = kernel.modules.categories()
            self.assertEqual(list(categories_data.keys()), ["Analytics", "Website"])
        finally:
            registry._modules = original_modules

    def test_dashboard_modules_returns_registered_widgets(self):
        original_widgets = kernel.widgets._widgets
        kernel.widgets._widgets = []

        try:
            register_widget(
                title="Widget A",
                template="cms/widgets/widget_a.html",
                order=20,
            )
            register_widget(
                title="Widget B",
                template="cms/widgets/widget_b.html",
                order=10,
            )

            widgets = kernel.widgets.enabled()

            self.assertEqual([widget.title for widget in widgets], ["Widget B", "Widget A"])
        finally:
            kernel.widgets._widgets = original_widgets

    def test_get_sidebar_modules_metadata(self):
        from apps.cms.services.navigation import get_sidebar_modules

        original_modules = registry._modules
        registry._modules = []

        try:
            register_module(
                name="Test Dashboard",
                icon="bi-speedometer",
                url_name="cms_dashboard",
                category="System",
                description="Test system dashboard",
                badge_callback=lambda: 5,
                order=5,
            )

            sidebar_data = get_sidebar_modules()
            self.assertIn("System", sidebar_data)
            modules = sidebar_data["System"]
            self.assertEqual(len(modules), 1)
            module_data = modules[0]
            self.assertEqual(module_data["title"], "Test Dashboard")
            self.assertEqual(module_data["description"], "Test system dashboard")
            self.assertEqual(module_data["icon"], "bi-speedometer")
            self.assertEqual(module_data["url"], "/cms/")
            self.assertEqual(module_data["url_name"], "cms_dashboard")
            self.assertEqual(module_data["badge"], 5)
        finally:
            registry._modules = original_modules

    def test_get_sidebar_modules_skips_broken_urls_without_crashing(self):
        from apps.cms.services.navigation import get_sidebar_modules

        original_modules = registry._modules
        registry._modules = []

        try:
            register_module(
                name="Broken Link",
                icon="bi-link",
                url_name="not-a-real-route",
                category="System",
                order=10,
            )

            sidebar_data = get_sidebar_modules()
            self.assertIn("System", sidebar_data)
            self.assertIsNone(sidebar_data["System"][0]["url"])
            self.assertEqual(sidebar_data["System"][0]["url_name"], "not-a-real-route")
        finally:
            registry._modules = original_modules

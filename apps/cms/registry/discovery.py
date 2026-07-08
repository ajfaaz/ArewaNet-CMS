from importlib import import_module

from django.apps import apps


def discover_modules():
    """
    Auto-import cms.py from every installed app.
    """

    for app in apps.get_app_configs():

        try:
            import_module(f"{app.name}.cms")

        except ModuleNotFoundError as exc:

            expected = f"{app.name}.cms"

            if exc.name == expected:
                continue

            raise

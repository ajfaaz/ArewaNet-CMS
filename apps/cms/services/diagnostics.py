from apps.cms.kernel import kernel


def registry_report():
    return {
        "modules": len(kernel.modules.all()),
        "widgets": len(kernel.widgets.all()),
        "categories": list(kernel.modules.categories().keys()),
    }
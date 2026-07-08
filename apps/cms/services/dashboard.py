from apps.cms.kernel import kernel


def get_dashboard_widgets(user=None):
    return kernel.widgets.enabled(user)

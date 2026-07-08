class CMSPlugin:

    name = ""

    version = "1.0"

    def ready(self):
        """
        Called when Django starts.
        """
        pass

    def install(self):
        """
        Called during installation.
        """
        pass

    def uninstall(self):
        """
        Called during removal.
        """
        pass

    def dashboard_widgets(self):
        return []

    def sidebar_modules(self):
        return []

    def permissions(self):
        return []

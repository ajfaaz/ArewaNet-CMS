class ComponentConfiguration:

    def __init__(self, component):
        self.component = component

    def get(self, key, default=None):
        return self.component.configuration.get(key, default)

    def set(self, key, value):
        self.component.configuration[key] = value

    def all(self):
        return self.component.configuration

from .components import registry

from apps.content.forms.hero import HeroComponentForm
from apps.content.renderers.hero import HeroRenderer

registry.register(
    component_type="hero",
    name="Hero",
    icon="fa-solid fa-desktop",
    renderer=HeroRenderer,
    form=HeroComponentForm,
    template="content/hero.html",
)

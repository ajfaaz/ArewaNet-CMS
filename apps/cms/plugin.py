from dataclasses import dataclass, field

from apps.cms.registry.module import CMSModule
from apps.cms.registry.widget import CMSWidget


@dataclass(slots=True)
class CMSPlugin:

    module: CMSModule

    widgets: list[CMSWidget] = field(
        default_factory=list
    )
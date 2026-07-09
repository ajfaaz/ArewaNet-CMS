from dataclasses import dataclass, field

from apps.cms.registry.module import CMSModule
from apps.cms.registry.widget import CMSWidget


@dataclass(slots=True)
class CMSPlugin:
    """
    Complete CMS plugin contributed by an application.
    """

    module: CMSModule

    widgets: list[CMSWidget] = field(default_factory=list)

    permissions: list[str] = field(default_factory=list)
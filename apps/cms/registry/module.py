from dataclasses import dataclass, field
from typing import Callable, List, Optional


@dataclass
class CMSModule:

    # =====================================================
    # Identity
    # =====================================================

    name: str

    icon: str

    url_name: str

    description: Optional[str] = None

    # =====================================================
    # Organization
    # =====================================================

    category: str = "General"

    order: int = 100

    color: str = "primary"

    # =====================================================
    # Security
    # =====================================================

    permission: Optional[str] = None

    enabled: bool = True

    # =====================================================
    # Dashboard
    # =====================================================

    widgets: List = field(default_factory=list)

    # =====================================================
    # Sidebar
    # =====================================================

    badge_callback: Optional[Callable] = None

    # =====================================================
    # Search
    # =====================================================

    searchable: bool = True

    # =====================================================
    # Future Extensions
    # =====================================================

    metadata: dict = field(default_factory=dict)

    # =====================================================
    # Helpers
    # =====================================================

    @property
    def has_permission(self):
        return bool(self.permission)

    @property
    def has_widgets(self):
        return bool(self.widgets)

    @property
    def badge_count(self):
        if callable(self.badge_callback):
            return self.badge_callback()
        return None

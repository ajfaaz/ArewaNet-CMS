from dataclasses import dataclass, field
from typing import Callable


@dataclass(slots=True)
class CMSWidget:
    title: str
    template: str
    order: int = 100
    permission: str | None = None
    callback: Callable | None = None
    icon: str = ""
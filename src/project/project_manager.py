"""Project management module (stub implementation)."""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class ProjectInfo:
    name: str
    path: Path
    is_dirty: bool = False


class ProjectManager:
    def __init__(self) -> None:
        self.current: Optional[ProjectInfo] = None

    def new(self, name: str, path: Path) -> ProjectInfo:
        self.current = ProjectInfo(name=name, path=path)
        return self.current

    def mark_dirty(self, dirty: bool = True) -> None:
        if self.current is None:
            raise RuntimeError("No project loaded")
        self.current.is_dirty = dirty

    def status_line(self) -> str:
        if self.current is None:
            return "No project"
        marker = "*" if self.current.is_dirty else ""
        return f"{self.current.name}{marker} @ {self.current.path}"

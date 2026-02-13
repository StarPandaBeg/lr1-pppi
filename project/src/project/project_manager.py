"""Project management module."""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class ProjectInfo:
    """Immutable project metadata."""
    name: str
    """Project name."""
    path: Path
    """Filesystem location of the project."""
    is_dirty: bool = False
    """Dirty flag for unsaved changes."""


class ProjectManager:
    """Service for creating and tracking projects."""
    def __init__(self) -> None:
        """Initialize manager without an active project."""
        self.current: Optional[ProjectInfo] = None

    def new(self, name: str, path: Path) -> ProjectInfo:
        """
        Create a new project and set it as active.

        Args:
            name: Project name.
            path: Filesystem location.

        Returns:
            Project info object.
        """
        self.current = ProjectInfo(name=name, path=path)
        return self.current

    def mark_dirty(self, dirty: bool = True) -> None:
        """
        Mark the active project as modified.

        Args:
            dirty: New dirty flag value.
        """
        if self.current is None:
            raise RuntimeError("No project loaded")
        self.current.is_dirty = dirty

    def status_line(self) -> str:
        """
        Build a status line for UI display.

        Returns:
            Text with current project and dirty marker.
        """
        if self.current is None:
            return "No project"
        marker = "*" if self.current.is_dirty else ""
        return f"{self.current.name}{marker} @ {self.current.path}"

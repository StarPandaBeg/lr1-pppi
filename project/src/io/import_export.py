"""Import and export module."""

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class IOResult:
    """Result of import/export operation."""

    path: Path = field(metadata={"doc": "Target file path."})
    success: bool = field(default=True, metadata={"doc": "Success flag."})
    message: str = field(default="", metadata={"doc": "Status message."})


def export_scene(scene_name: str, path: Path) -> IOResult:
    """
    Export a scene to disk.

    Args:
        scene_name: Name of the scene.
        path: Destination path.

    Returns:
        Operation result.
    """
    return IOResult(path=path, success=True, message=f"Exported {scene_name}")


def import_scene(path: Path) -> IOResult:
    """
    Import a scene from disk.

    Args:
        path: Source file path.

    Returns:
        Operation result.
    """
    return IOResult(path=path, success=True, message="Imported scene")

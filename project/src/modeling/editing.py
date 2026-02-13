"""Polygon editing module."""

from dataclasses import dataclass, field


@dataclass
class Selection:
    """Selection descriptor for polygon editing."""

    vertices: int = field(metadata={"doc": "Selected vertices count."})
    edges: int = field(metadata={"doc": "Selected edges count."})
    faces: int = field(metadata={"doc": "Selected faces count."})


def extrude(selection: Selection, distance: float) -> Selection:
    """
    Extrude selected faces.

    Args:
        selection: Current selection.
        distance: Extrusion distance.

    Returns:
        Updated selection after extrusion.
    """
    return Selection(
        vertices=selection.vertices + selection.faces * 4,
        edges=selection.edges + selection.faces * 4,
        faces=selection.faces * 2,
    )


def bevel(selection: Selection, segments: int) -> Selection:
    """
    Bevel selected elements.

    Args:
        selection: Current selection.
        segments: Number of bevel segments.

    Returns:
        Updated selection after bevel.
    """
    return Selection(
        vertices=selection.vertices + segments,
        edges=selection.edges + segments * 2,
        faces=selection.faces + segments,
    )

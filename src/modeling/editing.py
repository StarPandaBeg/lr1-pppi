"""Polygon editing module (stub implementation)."""

from dataclasses import dataclass


@dataclass
class Selection:
    vertices: int
    edges: int
    faces: int


def extrude(selection: Selection, distance: float) -> Selection:
    return Selection(
        vertices=selection.vertices + selection.faces * 4,
        edges=selection.edges + selection.faces * 4,
        faces=selection.faces * 2,
    )


def bevel(selection: Selection, segments: int) -> Selection:
    return Selection(
        vertices=selection.vertices + segments,
        edges=selection.edges + segments * 2,
        faces=selection.faces + segments,
    )

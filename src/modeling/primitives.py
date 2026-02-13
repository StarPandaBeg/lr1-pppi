"""Geometric primitives module."""

from dataclasses import dataclass, field


@dataclass
class Mesh:
    """Lightweight mesh descriptor."""

    name: str = field(metadata={"doc": "Mesh name."})
    vertex_count: int = field(metadata={"doc": "Number of vertices."})


def create_cube(size: float) -> Mesh:
    """
    Create a cube primitive.

    Args:
        size: Edge length.

    Returns:
        New mesh instance.
    """
    return Mesh(name=f"Cube({size})", vertex_count=8)


def create_sphere(radius: float, segments: int) -> Mesh:
    """
    Create a sphere primitive.

    Args:
        radius: Sphere radius.
        segments: Number of segments.

    Returns:
        New mesh instance.
    """
    verts = max(12, segments * segments)
    return Mesh(name=f"Sphere(r={radius}, s={segments})", vertex_count=verts)

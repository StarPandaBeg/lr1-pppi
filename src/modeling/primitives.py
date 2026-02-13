"""Geometric primitives module (stub implementation)."""

from dataclasses import dataclass


@dataclass
class Mesh:
    name: str
    vertex_count: int


def create_cube(size: float) -> Mesh:
    return Mesh(name=f"Cube({size})", vertex_count=8)


def create_sphere(radius: float, segments: int) -> Mesh:
    verts = max(12, segments * segments)
    return Mesh(name=f"Sphere(r={radius}, s={segments})", vertex_count=verts)

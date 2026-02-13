"""Spatial transform module."""

from dataclasses import dataclass, field


@dataclass
class Vec3:
    """3D vector value object."""

    x: float = field(metadata={"doc": "X component."})
    y: float = field(metadata={"doc": "Y component."})
    z: float = field(metadata={"doc": "Z component."})


@dataclass
class Transform:
    """Position, rotation, and scale of an object."""

    position: Vec3 = field(
        default_factory=lambda: Vec3(0.0, 0.0, 0.0),
        metadata={"doc": "World position."},
    )
    rotation: Vec3 = field(
        default_factory=lambda: Vec3(0.0, 0.0, 0.0),
        metadata={"doc": "Euler rotation in degrees."},
    )
    scale: Vec3 = field(
        default_factory=lambda: Vec3(1.0, 1.0, 1.0),
        metadata={"doc": "Non-uniform scale."},
    )

    def translate(self, dx: float, dy: float, dz: float) -> None:
        """
        Apply translation to the position.

        Args:
            dx: Delta along X.
            dy: Delta along Y.
            dz: Delta along Z.
        """
        self.position = Vec3(
            self.position.x + dx,
            self.position.y + dy,
            self.position.z + dz,
        )

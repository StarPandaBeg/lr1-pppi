"""Spatial transform module (stub implementation)."""

from dataclasses import dataclass, field


@dataclass
class Vec3:
    x: float
    y: float
    z: float


@dataclass
class Transform:
    position: Vec3 = field(default_factory=lambda: Vec3(0.0, 0.0, 0.0))
    rotation: Vec3 = field(default_factory=lambda: Vec3(0.0, 0.0, 0.0))
    scale: Vec3 = field(default_factory=lambda: Vec3(1.0, 1.0, 1.0))

    def translate(self, dx: float, dy: float, dz: float) -> None:
        self.position = Vec3(
            self.position.x + dx,
            self.position.y + dy,
            self.position.z + dz,
        )

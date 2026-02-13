"""Camera module (stub implementation)."""

from dataclasses import dataclass, field
from .transform import Transform


@dataclass
class Camera:
    name: str
    fov_degrees: float = 60.0
    transform: Transform = field(default_factory=Transform)

    def set_fov(self, value: float) -> None:
        if value <= 0:
            raise ValueError("FOV must be positive")
        self.fov_degrees = value

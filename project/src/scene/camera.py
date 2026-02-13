"""Camera module."""

from dataclasses import dataclass, field

from .transform import Transform


@dataclass
class Camera:
    """Scene camera with field of view and transform."""

    name: str = field(metadata={"doc": "Camera name."})
    fov_degrees: float = field(default=60.0, metadata={"doc": "Field of view."})
    transform: Transform = field(
        default_factory=Transform,
        metadata={"doc": "Camera transform."},
    )

    def set_fov(self, value: float) -> None:
        """
        Update field of view.

        Args:
            value: New FOV in degrees.

        Raises:
            ValueError: If value is not positive.
        """
        if value <= 0:
            raise ValueError("FOV must be positive")
        self.fov_degrees = value

"""Lighting module."""

from dataclasses import dataclass, field


@dataclass
class Light:
    """Light source descriptor."""

    name: str = field(metadata={"doc": "Light name."})
    intensity: float = field(default=1.0, metadata={"doc": "Light intensity."})
    color: str = field(default="white", metadata={"doc": "Light color."})


def set_intensity(light: Light, value: float) -> None:
    """
    Update intensity for a light.

    Args:
        light: Target light.
        value: New intensity value.
    """
    light.intensity = max(0.0, value)

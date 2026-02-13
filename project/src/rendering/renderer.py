"""Rendering module."""

from dataclasses import dataclass, field


@dataclass
class RenderSettings:
    """Rendering settings descriptor."""

    width: int = field(default=800, metadata={"doc": "Output width."})
    height: int = field(default=600, metadata={"doc": "Output height."})
    samples: int = field(default=32, metadata={"doc": "Samples per pixel."})


def render_scene(scene_name: str, settings: RenderSettings) -> str:
    """
    Render a scene to an image.

    Args:
        scene_name: Name of the scene to render.
        settings: Rendering settings.

    Returns:
        Output image path.
    """
    return f"renders/{scene_name}_{settings.width}x{settings.height}.png"

"""Materials and texturing module."""

from dataclasses import dataclass, field


@dataclass
class Material:
    """Surface material with basic properties."""

    name: str = field(metadata={"doc": "Material name."})
    color: str = field(default="white", metadata={"doc": "Base color."})
    roughness: float = field(default=0.5, metadata={"doc": "Surface roughness."})
    metallic: float = field(default=0.0, metadata={"doc": "Metallic factor."})


def assign_material(object_name: str, material: Material) -> str:
    """
    Assign a material to an object.

    Args:
        object_name: Target object name.
        material: Material to assign.

    Returns:
        Status message.
    """
    return f"Material {material.name} assigned to {object_name}"

"""Procedural modifiers module."""

from dataclasses import dataclass, field


@dataclass
class Modifier:
    """Base modifier descriptor."""

    name: str = field(metadata={"doc": "Modifier name."})
    enabled: bool = field(default=True, metadata={"doc": "Enabled flag."})


class Mirror(Modifier):
    """Mirror modifier across a given axis."""

    def __init__(self, axis: str = "X") -> None:
        """
        Create mirror modifier.

        Args:
            axis: Axis name (X, Y, Z).
        """
        super().__init__(name=f"Mirror({axis})")


class Array(Modifier):
    """Array modifier duplicating the object."""

    def __init__(self, count: int) -> None:
        """
        Create array modifier.

        Args:
            count: Number of duplicates.
        """
        super().__init__(name=f"Array({count})")

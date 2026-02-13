"""Procedural modifiers module (stub implementation)."""

from dataclasses import dataclass


@dataclass
class Modifier:
    name: str
    enabled: bool = True


class Mirror(Modifier):
    def __init__(self, axis: str = "X") -> None:
        super().__init__(name=f"Mirror({axis})")


class Array(Modifier):
    def __init__(self, count: int) -> None:
        super().__init__(name=f"Array({count})")

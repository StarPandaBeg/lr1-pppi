"""Scene graph module (stub implementation)."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class SceneNode:
    name: str
    children: List["SceneNode"] = field(default_factory=list)

    def add_child(self, node: "SceneNode") -> None:
        self.children.append(node)

    def find(self, name: str) -> "SceneNode | None":
        if self.name == name:
            return self
        for child in self.children:
            found = child.find(name)
            if found is not None:
                return found
        return None


class Scene:
    def __init__(self) -> None:
        self.root = SceneNode("Root")

    def add_object(self, node: SceneNode) -> None:
        self.root.add_child(node)

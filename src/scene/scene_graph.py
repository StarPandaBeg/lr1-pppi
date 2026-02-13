"""Scene graph module."""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class SceneNode:
    """Node of the scene graph tree."""

    name: str = field(metadata={"doc": "Node name."})
    children: List["SceneNode"] = field(
        default_factory=list,
        metadata={"doc": "Child nodes in the hierarchy."},
    )

    def add_child(self, node: "SceneNode") -> None:
        """
        Attach a child node.

        Args:
            node: Node to attach.
        """
        self.children.append(node)

    def find(self, name: str) -> Optional["SceneNode"]:
        """
        Find a node by name in the subtree.

        Args:
            name: Target node name.

        Returns:
            The found node or None.
        """
        if self.name == name:
            return self
        for child in self.children:
            found = child.find(name)
            if found is not None:
                return found
        return None


class Scene:
    """Container for the scene graph."""

    def __init__(self) -> None:
        """Initialize a scene with a root node."""
        self.root = SceneNode("Root")

    def add_object(self, node: SceneNode) -> None:
        """
        Add an object to the root.

        Args:
            node: Node to add as a child of root.
        """
        self.root.add_child(node)

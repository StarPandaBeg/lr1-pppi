"""UI panels for the 3D editor."""

from dataclasses import dataclass


@dataclass
class PanelState:
    """Persistent state for a UI panel."""
    title: str
    """Panel title shown in the UI."""
    visible: bool = True
    """Visibility flag for the panel."""


class Panel:
    """Base panel widget."""
    def __init__(self, title: str) -> None:
        """
        Create a panel instance.

        Args:
            title: Panel title shown in the UI.
        """
        self.state = PanelState(title=title)

    def toggle(self) -> None:
        """Toggle panel visibility."""
        self.state.visible = not self.state.visible

    def render(self) -> str:
        """Return a textual representation of the panel."""
        status = "visible" if self.state.visible else "hidden"
        return f"[{self.state.title}] {status}"


class Toolbar(Panel):
    """Toolbar widget with a list of tools."""
    def __init__(self) -> None:
        """Initialize toolbar with a default title."""
        super().__init__("Toolbar")
        self.tools = []

    def add_tool(self, name: str) -> None:
        """
        Register a new tool.

        Args:
            name: Tool label.
        """
        self.tools.append(name)

    def render(self) -> str:
        """Return a textual representation of the toolbar."""
        base = super().render()
        return f"{base} | tools={', '.join(self.tools) or 'none'}"

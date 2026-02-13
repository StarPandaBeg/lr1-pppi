"""UI panels for the 3D editor (stub implementation)."""

from dataclasses import dataclass


@dataclass
class PanelState:
    title: str
    visible: bool = True


class Panel:
    def __init__(self, title: str) -> None:
        self.state = PanelState(title=title)

    def toggle(self) -> None:
        self.state.visible = not self.state.visible

    def render(self) -> str:
        status = "visible" if self.state.visible else "hidden"
        return f"[{self.state.title}] {status}"


class Toolbar(Panel):
    def __init__(self) -> None:
        super().__init__("Toolbar")
        self.tools = []

    def add_tool(self, name: str) -> None:
        self.tools.append(name)

    def render(self) -> str:
        base = super().render()
        return f"{base} | tools={', '.join(self.tools) or 'none'}"

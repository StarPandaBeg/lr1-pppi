"""UI panels for the 3D editor (alternate stub)."""

class Panel:
    def __init__(self, title: str, visible: bool = True) -> None:
        self.title = title
        self.visible = visible

    def show(self) -> None:
        self.visible = True

    def hide(self) -> None:
        self.visible = False

    def render(self) -> str:
        return f"{self.title}: {'on' if self.visible else 'off'}"

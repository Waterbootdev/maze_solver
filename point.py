class Point:
    def __init__(self, horizontal:float, vertical:float) -> None:
        self.x = horizontal
        self.y = vertical

    def __repr__(self) -> str:
        return f"[{self.x}, {self.y}]"

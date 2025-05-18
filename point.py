class Point:
    def __init__(self, horizontal:float, vertical:float) -> None:
        self.x = horizontal
        self.y = vertical

    def __repr__(self) -> str:
        return f"[{self.x}, {self.y}]"
    
    def mid_point(self, other):
        other_point:Point = other
        return Point(Point.mid(self.x, other_point.x), Point.mid(self.y, other_point.y))

    @staticmethod
    def mid(left:float, rigth:float) -> float:
        return left + (rigth - left) /2


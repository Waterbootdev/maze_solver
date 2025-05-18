from tkinter import Canvas
from point import Point
class Line:
    def __init__(self, first:Point, second:Point) -> None:
        self.first = first
        self.second = second

    def draw(self, canvas:Canvas, fill_color:str):
        print(self) 
        canvas.create_line(self.first.x, self.first.y, self.second.x, self.second.y, fill=fill_color, width=2)

    def __repr__(self) -> str:
        return f"[ {self.first} -> {self.second} ]"
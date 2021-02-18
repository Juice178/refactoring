from shape import Shape
from dataclasses import dataclass

@dataclass(frozen=True)
class ShapeRectangle(Shape):

    def get_name(self) -> str:
        return "RECTANGLE"
    
    def draw(self) -> None:
        print(f"drawRecangle: {self}")
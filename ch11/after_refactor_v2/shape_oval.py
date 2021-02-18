from shape import Shape
from dataclasses import dataclass

@dataclass(frozen=True)
class ShapeOval(Shape):

    def get_name(self) -> str:
        return "OVAL"
    
    def draw(self) -> None:
        print(f"drawOval: {self}")
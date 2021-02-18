from shape import Shape
from dataclasses import dataclass

@dataclass(frozen=True)
class ShapeLine(Shape):

    def get_name(self) -> str:
        return "LINE"
    
    def draw(self) -> None:
        print(f"drawLine: {self}")
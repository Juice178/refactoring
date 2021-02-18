from shape import Shape 


class ShapeLine(Shape):
    def __init__(self, startx: int, starty: int, endx: int, endy: int) -> None:
        super().__init__(startx, starty, endx, endy)

    def get_typecode(self) -> int:
        return Shape.TYPECODE_LINE

    def get_name(self) -> str:
        return "LINE"
    
    def draw(self) -> None:
        self.draw_line()

    def draw_line(self) -> None:
        print(f"drawLine: {self}")
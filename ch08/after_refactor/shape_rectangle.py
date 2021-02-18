from shape import Shape 


class ShapeRectangle(Shape):
    def __init__(self, startx: int, starty: int, endx: int, endy: int) -> None:
        super().__init__(startx, starty, endx, endy)

    def get_typecode(self) -> int:
        return Shape.TYPECODE_RENCTANGLE

    def get_name(self) -> str:
        return "RECTANGLE"
    
    def draw(self) -> None:
        self.draw_rectangle()

    def draw_rectangle(self) -> None:
        print(f"drawRectangle: {self}")
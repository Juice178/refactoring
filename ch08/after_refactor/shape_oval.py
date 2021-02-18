from shape import Shape 


class ShapeOval(Shape):
    def __init__(self, startx: int, starty: int, endx: int, endy: int) -> None:
        super().__init__(startx, starty, endx, endy)

    def get_typecode (self) -> int:
        return Shape.TYPECODE_OVAL

    def get_name(self) -> str:
        return "OVAL"
    
    def draw(self) -> None:
        self.draw_oval()

    def draw_oval(self) -> None:
        print(f"drawOval: {self}")
from typing import Final

class Shape:
    TYPECODE_LINE: Final[int] = 0
    TYPECODE_RECTANGLE: Final[int] = 1
    TYPECODE_OVAL: Final[int] = 2

    def __init__(self, typcode: int, startx: int, starty: int, 
                 endx: int, endy: int) -> None:
        self._typcode = typcode
        self._startx = startx 
        self._endx = endx
        self._starty = starty
        self._endy = endy

    def get_typecode(self) -> int:
        return self._typcode

    def get_name(self) -> str:
        if self._typcode == self.TYPECODE_LINE:
            return "LINE"
        elif self._typcode == self.TYPECODE_RECTANGLE:
            return "RECTANGLE"
        elif self._typcode == self.TYPECODE_OVAL:
            return "OVAL"
        else:
            return None

    def __str__(self) -> str:
        # return f"[ {self.get_name()}, ( {self._startx} , {self._starty} ) - ( {self._endx} , {self._endy} )"
        return (f"[ {self.get_name()}"
               f"({self._startx} , {self._starty})"
               "-"
               f"({self._endx} , {self._endy})"
               "]")
               )

    def draw(self) -> None:
        if self._typcode == self.TYPECODE_LINE:
            self.draw_line()
        elif self._typcode == self.TYPECODE_RECTANGLE:
            self.draw_rectangle()
        elif self._typcode == self.TYPECODE_OVAL:
            self.draw_oval()
        else:
            pass

    def draw_line(self) -> None:
        print(f"drawLine: {self}")

    def draw_rectangle(self) -> None:
        print(f"drawRectangle: {self}")

    def draw_oval(self) -> None:
        print(f"drawOval: {self}")

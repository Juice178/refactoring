from __future__ import annotations
from typing import Final
from abc import ABC, abstractmethod
# from shape_line import ShapeLine
# from shape_rectangle import ShapeRectangle
# from shape_oval import ShapeOval



class Shape(ABC):
    TYPECODE_LINE: Final[int] = 0
    TYPECODE_RECTANGLE: Final[int] = 1
    TYPECODE_OVAL: Final[int] = 2

    @staticmethod
    def create_shape(typecode: int, startx: int, starty: int, endx: int, endy: int) -> Shape:
        from shape_line import ShapeLine
        from shape_rectangle import ShapeRectangle
        from shape_oval import ShapeOval

        if typecode == Shape.TYPECODE_LINE:
            return ShapeLine(startx, starty, endx, endy)
        elif typecode == Shape.TYPECODE_RECTANGLE:
            return ShapeRectangle(startx, starty, endx, endy)
        elif typecode == Shape.TYPECODE_OVAL:
            return ShapeOval(startx, starty, endx, endy)
        else:
            raise Exception(f"typcode = {typecode}")

    def __init__(self, startx: int, starty: int, endx: int, endy: int) -> None:
        self._startx = startx
        self._endx = endx
        self._starty = starty
        self._endy = endy

    @abstractmethod
    def get_typecode(self) -> int:
        pass 

    @abstractmethod
    def get_name(self) -> str:
        pass

    def __str__(self) -> str:
        # return f"[ {self.get_name()}, ( {self._startx} , {self._starty} ) - ( {self._endx} , {self._endy} )"
        return (f"[ {self.get_name()}"
               f"({self._startx} , {self._starty})"
                "-"
               f"({self._endx} , {self._endy})"
               "]")
    @abstractmethod
    def draw(self) -> None:
        pass

from __future__ import annotations
from dataclasses import dataclass
from typing import Final, ClassVar

@dataclass(frozen=True)
class Shape:
    TYPECODE_LINE: ClassVar[int] = 0
    TYPECODE_RECTANGLE: ClassVar[int] = 1
    TYPECODE_OVAL: ClassVar[int] = 2

    _typecode: int
    _startx: int
    _starty: int
    _endx: int
    _endy: int
    
    @staticmethod
    def create(typecode: int, startx: int, starty: int, endx: int, endy:int) -> Shape:
        return Shape(typecode, startx, starty, endx, endy)

    def get_type(self) -> int:
        return self._typecode

    def get_name(self) -> str:
        if self._typecode == Shape.TYPECODE_LINE:
            return "LINE"
        elif self._typecode == Shape.TYPECODE_RECTANGLE:
            return "RECTANGLE"
        elif self._typecode == Shape.TYPECODE_OVAL:
            return "OVAL"
        else:
            return None

    def __str__(self) -> str:
        return f"[ {self.get_name()}, ({self._startx}, {self._starty})-({self._endx}, {self._endy})"

    def draw(self) -> None:
        if self._typecode == Shape.TYPECODE_LINE:
            self.draw_line()
        elif self._typecode == Shape.TYPECODE_RECTANGLE:
            self.draw_rectangle()
        elif self._typecode == Shape.TYPECODE_OVAL:
            self.draw_oval()
        else:
            pass

    def draw_line(self) -> None:
        print(f"drawLine: {self}")

    def draw_rectangle(self) -> None:
        print(f"drawRectangle: {self}")

    def draw_oval(self) -> None:
        print(f"drawOval: {self}")


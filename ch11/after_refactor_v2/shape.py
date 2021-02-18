from __future__ import annotations
from dataclasses import dataclass
from typing import ClassVar
from abc import ABC, abstractmethod


@dataclass(frozen=True)
class Shape(ABC):
    TYPECODE_LINE: ClassVar[int] = 0
    TYPECODE_RECTANGLE: ClassVar[int] = 1
    TYPECODE_OVAL: ClassVar[int] = 2

    _typecode: int
    _startx: int
    _starty: int
    _endx: int
    _endy: int
    
    @staticmethod
    def create_line(typecode: int, startx: int, starty: int, endx: int, endy:int) -> Shape:
        from shape_line import ShapeLine
        return ShapeLine(typecode, startx, starty, endx, endy)
    
    @staticmethod
    def create_rectangle(typecode: int, startx: int, starty: int, endx: int, endy:int) -> Shape:
        from shape_rectangle import ShapeRectangle
        return ShapeRectangle(typecode, startx, starty, endx, endy)

    @staticmethod
    def create_oval(typecode: int, startx: int, starty: int, endx: int, endy:int) -> Shape:
        from shape_oval import ShapeOval
        return ShapeOval(typecode, startx, starty, endx, endy)

    def __str__(self) -> str:
        return f"[ {self.get_name()}, ({self._startx}, {self._starty})-({self._endx}, {self._endy})"

    @abstractmethod
    def get_name(self) -> str:
        pass 

    @abstractmethod
    def draw(self) -> None:
        pass
    



from __future__ import annotations
from typing import Final
from enum import Enum

class ItemType(Enum):
    BOOK = 0
    DVD = 1
    SOFTWARE = 2

    def __init__(self, typecode: int) -> None:
        self._typecode: Final[int] = typecode

    def get_typecode(self) -> int:
        return self._typecode

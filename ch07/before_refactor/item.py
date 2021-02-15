from typing import Final

class Item:
    TYPECODE_BOOK: Final[int] = 0
    TYPECODE_DVD: Final[int] = 1
    TYPECODE_SOFTWARE: Final[int] = 2

    def __init__(self, typecode: int, title: str, price: int) -> None:
        self._typecode: Final[int] = typecode
        self._title = title
        self._price = price

    def get_typecode(self) -> int:
        return self._typecode

    def get_title(self) -> str:
        return self._title 

    def get_price(self) -> int:
        return self._price

    def __str__(self) -> str:
        return f"[ {self.get_typecode()}, {self.get_title()}, {self.get_price()} ]"





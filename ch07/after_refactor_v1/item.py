from typing import Final
from item_type import ItemType


class Item:
    def __init__(self, item_type: ItemType, title: str, price: int) -> None:
        self._item_type: Final[ItemType] = item_type
        self._title = title
        self._price = price

    def get_title(self) -> str:
        return self._title 

    def get_price(self) -> int:
        return self._price

    def __str__(self) -> str:
        return f"[ {self._item_type.get_typecode()}, {self.get_title()}, {self.get_price()} ]"





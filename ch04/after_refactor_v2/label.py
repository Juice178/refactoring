from __future__ import annotations
from typing import Final

class Label:
    def __init__(self, label: str) -> None:
        self._label = label 
    
    def display(self):
        print(f"display: {self._label}")

    def __str__(self) -> str:
        return f"{self._label}"

    def is_null(self) -> bool:
        return False

    # Factory Method
    @staticmethod
    def new_null() -> Label:
        return NullLabel.get_instance()

    
class NullLabel(Label):
    #singleton: Final[NullLabel] = NullLabel()
    # Singleton
    singleton = None
    
    @staticmethod
    def get_instance() -> NullLabel:
        if NullLabel.singleton is None:
            NullLabel.singleton = NullLabel()
        return NullLabel.singleton

    def __init__(self) -> None:
        super().__init__("(none)")

    def display(self) -> None:
        pass

    def is_null(self) -> bool:
        return True
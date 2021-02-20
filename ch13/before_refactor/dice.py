from random import Random
from dataclasses import dataclass
from exceptions import UnsupportedOperationException
from typing import Optional, Any, Final


@dataclass()
class Dice(Random):
    x: Final[Optional[int]] = None

    def __post_init__(self):
        self.seed(self.x)
    
    def next_int(self) -> int:
        return self.randint(1, 6)

    def betavariat(self) -> float:
        raise UnsupportedOperationException()

    def gauss(self) -> float:
        raise UnsupportedOperationException()

    def choice(self) -> Any:
        raise UnsupportedOperationException()

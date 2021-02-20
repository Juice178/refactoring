from random import Random
from dataclasses import dataclass
from exceptions import UnsupportedOperationException
from typing import Optional, Any, Final


@dataclass()
class Dice:
    x: Final[Optional[int]] = None

    def __post_init__(self):
        self._random = Random(self.x)
    
    def next_int(self) -> int:
        return self._random.randint(1, 6)

    def seed(self, x: int) -> None:
        self._random.seed(x)

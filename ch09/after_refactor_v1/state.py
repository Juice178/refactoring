from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def get_typecode(self) -> int:
        pass
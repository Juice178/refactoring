from typing import Final, List

class SortSample:
    # _data: Final[List[int]] = []

    def __init__(self, data: List[int]) -> None:
        self._data = data.copy()

    def sort(self) -> None:
        for x in range(len(self._data)-1):
            m = x
            for y in range(x+1, len(self._data)):
                if self._data[m] > self._data[y]:
                    m = y 
            assert self.is_min(m, x, len(self._data)-1)
            v = self._data[m]
            self._data[m] = self._data[x]
            self._data[x] = v
            assert self.is_sorted(0, x+1)

    def __str__(self) -> str:
        buffer = []
        buffer.append("[")
        for i in range(len(self._data)):
            buffer.append(str(self._data[i]))
            buffer.append(", ")
        buffer.append("]")
        return ''.join(buffer)

    
    def is_min(self, pos: int, start: int, end: int) -> bool:
        for i in range(start, end+1):
            if self._data[pos] > self._data[i]:
                return False 
        return True 

    def is_sorted(self, start: int, end: int) -> bool:
        for i in range(start, end):
            if self._data[i] > self._data[i+1]:
                return False
        return True


from typing import Final, List

class SortSample:
    # _data: Final[List[int]] = []

    def __init__(self, data: List[int]):
        self._data = data.copy()

    def sort(self):
        for x in range(len(self._data)-1):
            m = x
            for y in range(x+1, len(self._data)):
                if self._data[m] > self._data[y]:
                    m = y 
            # _data[m] should be the minimal value in _data[x] ~ data[len(data)-1]
            v = self._data[m]
            self._data[m] = self._data[x]
            self._data[x] = v
            # _data[0] ~ _data[x+1] should have been sorted

    def __str__(self) -> str:
        buffer = []
        buffer.append("[")
        for i in range(len(self._data)):
            buffer.append(str(self._data[i]))
            buffer.append(", ")
        buffer.append("]")
        return ''.join(buffer)

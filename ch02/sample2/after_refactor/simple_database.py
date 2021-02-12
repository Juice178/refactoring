from buffered_reader import BufferedReader
from string_buffer import StringBuffer


class SimpleDatabase:
    _map = dict()
    def __init__(self, r1: str) -> None:
        reader = BufferedReader(r1)
        while True:
            line = reader.read_line()
            if line == '':
                break
            equal_index = line.index("=")
            if equal_index > 0:
                key = line[0:equal_index]
                value = line[equal_index+1:len(line)]
                self._map[key] = value

    def put_value(self, key: str, value: str) -> None:
        self._map[key] = value 
    
    def get_value(self, key: str) -> str:
        return self._map[key]

    def iterator(self) -> iter:
        # print(self._map.keys())
        return iter(self._map.keys())
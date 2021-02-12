from buffered_reader import BufferedReader
from string_buffer import StringBuffer


class SimpleDatabase:
    _map = dict()
    def __init__(self, r1: str) -> None:
        r2 = BufferedReader(r1)
        flag = False
        tmp = None
        while not flag:
            tmp = r2.read_line()
            if tmp == '':
                flag = True 
            else:
                flag2 = True
                s1 = StringBuffer()
                s2 = StringBuffer()
                for i in range(len(tmp)):
                    tmp2 = tmp[i]
                    if flag2:
                        if tmp2 == '=':
                            flag2 = False 
                        else:
                            s1.append(tmp2)
                    else:
                        s2.append(tmp2)
                ss1 = s1.to_string()
                ss2 = s2.to_string()
                self._map[ss1] = ss2 
    
    def put_value(self, key: str, value: str) -> None:
        self._map[key] = value 
    
    def get_value(self, key: str) -> str:
        return self._map[key]

    def iterator(self) -> iter:
        # print(self._map.keys())
        return iter(self._map.keys())
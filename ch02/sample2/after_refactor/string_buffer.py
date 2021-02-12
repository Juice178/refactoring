class StringBuffer:
    def __init__(self) -> None:
         self._strings = []
    
    def append(self, string: str) -> None: 
        self._strings.append(string)
    
    def to_string(self) -> str:
        return "".join(self._strings)
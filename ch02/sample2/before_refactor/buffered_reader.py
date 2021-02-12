class BufferedReader:
    def __init__(self, filename: str) -> None:
        self._file = open(filename, "r")

    def read_line(self) -> str:
        return self._file.readline()

    def close(self) -> None:
        self._file.close()
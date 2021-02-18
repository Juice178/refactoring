class Position:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y 

    def relative_move(self, dx: int, dy: int) -> None:
        self._x += dx
        self._y += dy
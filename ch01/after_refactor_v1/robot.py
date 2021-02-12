from typing import Final


class Robot:
    COMAMND_WALK: Final[int] = 0
    COMAMND_STOP: Final[int] = 1
    COMAMND_JUMP: Final[int] = 2
    _name: Final[str] = None

    def __init__(self, name: str) -> None:
        self._name = name

    def order(self, command: int) -> None:
        if command == self.COMAMND_WALK:
            print(f"{self._name} walks.")
        elif command == self.COMAMND_STOP:
            print(f"{self._name} stops.")
        elif command == self.COMAMND_JUMP:
            print(f"{self._name} jumps.")
        else:
            print(f"Command error. command = {command}")
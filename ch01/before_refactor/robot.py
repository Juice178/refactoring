from typing import Final


class Robot:
    _name: Final[str] = None

    def __init__(self, name: str) -> None:
        self._name = name

    def order(self, command: int) -> None:
        if command == 0:
            print(f"{self._name} walks.")
        elif command == 1:
            print(f"{self._name} stops.")
        elif command == 2:
            print(f"{self._name} jumps.")
        else:
            print(f"Command error. command = {command}")
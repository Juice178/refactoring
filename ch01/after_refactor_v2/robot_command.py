from typing import Final


class RobotCommand:
    _name: Final[str] = None

    def __init__(self, name: str) -> None:
        self._name = name 

    def __str__(self) -> str:
        return f"[ RobotCommand: {self._name} ]"
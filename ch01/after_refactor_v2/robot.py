from typing import Final
from robot_command import RobotCommand

class Robot:
    _name: Final[str] = None
    COMAMND_WALK: Final[RobotCommand] = RobotCommand("WALK")
    COMAMND_STOP: Final[RobotCommand] = RobotCommand("STOP")
    COMAMND_JUMP: Final[RobotCommand] = RobotCommand("JUMP")

    def __init__(self, name: str) -> None:
        self._name = name

    def order(self, command: RobotCommand) -> None:
        if command == self.COMAMND_WALK:
            print(f"{self._name} walks.")
        elif command == self.COMAMND_STOP:
            print(f"{self._name} stops.")
        elif command == self.COMAMND_JUMP:
            print(f"{self._name} jumps.")
        else:
            print(f"Command error. command = {command}")
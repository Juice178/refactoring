from typing import Final
from functools import singledispatchmethod
from position import Position
from direction import Direction
from command import Command
from invalid_command_exception import InvalidCommandException


class Robot:
    def __init__(self, name: str) -> None:
        self._name: Final[str] = name
        self._position: Final[Position] = Position(0, 0)
        self._direction: Final[Direction] = Direction(0, 1)

    def execute(self, command_sequence: str) -> None:
        tokens = command_sequence.split()
        try:
            for token in tokens:
                self.execute_command(token)
        except InvalidCommandException as e:
            print(f"Invalid command: {e}")

    @singledispatchmethod
    def execute_command(self, arg) -> bool:
        raise NotImplementedError("Method: execute_command is not implemented.")

    @execute_command.register
    def _(self, command_str: str) -> bool:
        command = Command.parseCommand(command_str)
        self.execute_command(command)

    @execute_command.register
    def _(self, command: Command) -> bool:
        if command == Command.FORWARD:
            self._position.relative_move(self._direction._x, self._direction._y)
        elif command == command.BACKWARD:
            self._position.relative_move(-self._direction._x, -self._direction._y)
        elif command == command.TURN_RIGHT:
            self._direction.set_direction(self._direction._y, -self._direction._x)
        elif command == command.TURN_LEFT:
            self._direction.set_direction(-self._direction._y, self._direction._x)
        else:
            raise InvalidCommandException(command.get_name())
        return True

    def __str__(self) -> str:
        return f"[ Robot: {self._name} position({self._position._x},{self._position._y}), \
                direction({self._direction._x}, {self._direction._y}) ]"



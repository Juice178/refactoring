from __future__ import annotations
from typing import Final, Dict
from invalid_command_exception import InvalidCommandException


class Command:
    FORWARD = None
    BACKWARD = None
    TURN_RIGHT = None
    TURN_LEFT = None
    _command_named_map = dict()

    def __init__(self, name: str) -> None:
        self._name = name
    
    @staticmethod
    def init_commands() -> None:
        Command.FORWARD = Command("forward")
        Command.BACKWARD = Command("backward")
        Command.TURN_RIGHT = Command("right")
        Command.TURN_LEFT = Command("left")

    @staticmethod
    def map_name_to_commands() -> None:
        Command._command_named_map[Command.FORWARD._name] = Command.FORWARD
        Command._command_named_map[Command.BACKWARD._name] = Command.BACKWARD
        Command._command_named_map[Command.TURN_RIGHT._name] = Command.TURN_RIGHT
        Command._command_named_map[Command.TURN_LEFT._name] = Command.TURN_LEFT
    
    def get_name(self) -> str:
        return self._name

    @staticmethod
    def parseCommand(name: str) -> Command:
        Command.init_commands()
        Command.map_name_to_commands()
        if not name in Command._command_named_map:
            raise InvalidCommandException(name)
        return Command._command_named_map.get(name)

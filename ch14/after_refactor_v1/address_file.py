from database import Database
from dataclasses import dataclass, field, InitVar
from typing import Final
from collections.abc import KeysView


@dataclass()
class AddressFile:
    _database: Final[Database] = field(default=None, init=False)
    _section: Final[str] = field(default=None, init=False)
    filename: InitVar[str] = None
    section: InitVar[str] = None


    def __post_init__(self, filename: str, section: str) -> None:
        self._section = section
        self._database = Database(filename=filename, section=section)

    def names(self) -> KeysView:
        return self._database.get_properties().keys()

    def set(self, key: str, value: str) -> None:
        self._database.set(key, value)

    def get(self, key: str) -> str:
        return self._database.get(key)

    def update(self) -> None:
        self._database.update()


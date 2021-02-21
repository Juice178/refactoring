from dataclasses import dataclass, InitVar, field
from typing import Final
from enum import Enum
from configparser import ConfigParser


@dataclass()
class Database:
    _properties: Final[ConfigParser] = field(default=None, init=False)
    _filename: Final[str] = field(default=None, init=False)
    _section: Final[str] = field(default=None, init=False)
    filename: InitVar[str] = None
    section: InitVar[str] = None

    def __post_init__(self, filename: str, section: str) -> None:
        self._filename = filename
        self._section = section
        self._properties = ConfigParser()
        self._properties[self._section] = {}
        # self._properties.read(self._filename)

    def set(self, key: str, value: str) -> None:
        self._properties[self._section][key] = value
    
    def get(self, key: str) -> str:
        return self._properties.get(self._section, key)

    def update(self) -> None:
        with open(self._filename, 'w') as configfile:
            self._properties.write(configfile)

    def keys(self) -> None:
        return self._properties[self._section].keys()

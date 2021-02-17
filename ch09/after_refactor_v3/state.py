from abc import ABCMeta, abstractmethod
from enum import Enum, EnumMeta
from state_stopped import StateStopped
from state_logging import StateLogging


class ABCEnumMeta(ABCMeta, EnumMeta):
    pass


class State(Enum, metaclass=ABCEnumMeta):
    STATE_STOPPED = StateStopped
    # STATE_STOPPED.log("test")
    STATE_LOGGING = StateLogging

    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

    @abstractmethod
    def log(self, info: str) -> None:
        pass
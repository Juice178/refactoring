from state import State
from logger import Logger


class StateStopped(State):
    def __init__(self) -> None:
        pass 

    def get_typecode(self) -> int:
        return Logger.STATE_STOPPED
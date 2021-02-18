from typing import Final
from state import State, STATE_STOPPED


class Logger:
    # STATE_STOPPED: Final[int] = 0
    # STATE_LOGGING: Final[int] = 1

    def __init__(self) -> None:
        self.set_state(State.STATE_STOPPED)

    def get_state(self) -> State:
        return self._state

    def set_state(self, state: State) -> None:
        self._state = state

    def start(self) -> None:
        if self.get_state() == State.STATE_STOPPED:
            print("** START LOGGING **")
            self.set_state(State.STATE_LOGGING)
        elif self.get_state() == State.STATE_LOGGING:
            # Do nothing
            pass
        else:
            print(f"Invalid state: {self.get_state()}")

    def stop(self) -> None:
        if self.get_state() == State.STATE_STOPPED:
            # Do nothing
            pass
        elif self.get_state() == State.STATE_LOGGING:
            print("** STOP LOGGING **")
            self.set_state(State.STATE_STOPPED)
        else:
            print(f"Invalid state: {self.get_state()}")

    
    def log(self, info: str) -> None:
        if self.get_state() == State.STATE_STOPPED:
            print(f"Ignoring: {info}")
        elif self.get_state() == State.STATE_LOGGING:
            print(f"Logging: {info}")
            self.set_state(State.STATE_STOPPED)
        else:
            print(f"Invalid state: {self.get_state()}")



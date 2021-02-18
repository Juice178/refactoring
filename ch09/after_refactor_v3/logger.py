from typing import Final
from state import State


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
        self._state.value.start(self._state)
        self.set_state(State.STATE_LOGGING)

    def stop(self) -> None:
        self._state.value.stop(self._state)
        self.set_state(State.STATE_LOGGING)

    def log(self, info: str) -> None:
        self._state.value.log(self._state, info)



from typing import Final
# import state_stopped.StateStopped as StateStopped
# import state_logging.StateLogging as StateLogging
# from state_stopped import StateStopped
# from state_logging import StateLogging


class Logger:
    STATE_STOPPED: Final[int] = 0
    STATE_LOGGING: Final[int] = 1

    def __init__(self) -> None:
        self.set_state(Logger.STATE_STOPPED)

    def get_state(self) -> int:
        return self._state.get_typecode()

    def set_state(self, state: int) -> None:
        from state_stopped import StateStopped
        from state_logging import StateLogging

        if state == Logger.STATE_STOPPED:
            self._state = StateStopped()
        elif state == Logger.STATE_LOGGING:
            self._state = StateLogging()
        else:
            print(f"Invalid state: {self._state}")

    def start(self) -> None:
        if self.get_state() == Logger.STATE_STOPPED:
            print("** START LOGGING **")
            self.set_state(Logger.STATE_LOGGING)
        elif self.get_state() == Logger.STATE_LOGGING:
            # Do nothing
            pass
        else:
            print(f"Invalid state: {self.get_state()}")

    def stop(self) -> None:
        if self.get_state() == Logger.STATE_STOPPED:
            # Do nothing
            pass
        elif self.get_state() == Logger.STATE_LOGGING:
            print("** STOP LOGGING **")
            self.set_state(Logger.STATE_STOPPED)
        else:
            print(f"Invalid state: {self.get_state()}")

    
    def log(self, info: str) -> None:
        if self.get_state() == Logger.STATE_STOPPED:
            print(f"Ignoring: {info}")
        elif self.get_state() == Logger.STATE_LOGGING:
            print(f"Logging: {info}")
            self.set_state(Logger.STATE_STOPPED)
        else:
            print(f"Invalid state: {self.get_state()}")



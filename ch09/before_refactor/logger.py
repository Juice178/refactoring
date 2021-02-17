from typing import Final

class Logger:
    STATE_STOPPED: Final[int] = 0
    STATE_LOGGING: Final[int] = 1

    def __init__(self) -> None:
        self._state = Logger.STATE_STOPPED

    def start(self) -> None:
        if self._state == Logger.STATE_STOPPED:
            print("** START LOGGING **")
            self._state = Logger.STATE_LOGGING
        elif self._state == Logger.STATE_LOGGING:
            # Do nothing
            pass
        else:
            print(f"Invalid state: {self._state}")

    def stop(self) -> None:
        if self._state == Logger.STATE_STOPPED:
            # Do nothing
            pass
        elif self._state == Logger.STATE_LOGGING:
            print("** STOP LOGGING **")
            self._state = self.STATE_STOPPED
        else:
            print(f"Invalid state: {self._state}")

    
    def log(self, info: str) -> None:
        if self._state == Logger.STATE_STOPPED:
            print(f"Ignoring: {info}")
        elif self._state == Logger.STATE_LOGGING:
            print(f"Logging: {info}")
            self._state = self.STATE_STOPPED
        else:
            print(f"Invalid state: {self._state}")



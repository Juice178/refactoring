from enum import Enum

class StateLogging(Enum):
    def start(self) -> None:
        # Do nothing
        pass
    
    def stop(self) -> None:
        print("** STOP LOGGING **")
    
    def log(self, info: str) -> None:
        print(f"Ignoring: {info}")

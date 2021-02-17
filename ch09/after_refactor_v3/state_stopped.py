from enum import Enum

class StateStopped(Enum):
    def __init__(self) -> None:
        pass

    def start(self) -> None:
        print("** START LOGGING **")
    
    def stop(self) -> None:
        # Do nothing
        pass
        
    def log(self, info: str) -> None:
        print(f"Ignoring: {info}")
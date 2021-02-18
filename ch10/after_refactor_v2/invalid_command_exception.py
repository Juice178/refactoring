class InvalidCommandException(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(name)
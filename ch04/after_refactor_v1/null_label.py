from label import Label

class NullLabel(Label):
    def __init__(self) -> None:
        super().__init__("(none)")

    def display(self) -> None:
        pass

    def is_null(self) -> bool:
        return True
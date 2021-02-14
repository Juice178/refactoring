class Label:
    def __init__(self, label: str) -> None:
        self._label = label 
    
    def display(self):
        print(f"display: {self._label}")

    def __str__(self) -> str:
        return f"{self._label}"

    def is_null(self) -> bool:
        return False
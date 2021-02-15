from typing import Final


class Banner:
    def __init__(self, content: str) -> None:
        self._content: Final[str] = content

    def print(self, times: int) -> None:
        # Prints border.
        print("+",  end="")
        for _ in range(len(self._content)):
            print("-", end="")
        print("+")

        # Prints content.
        for _ in range(times):
            print(f"| {self._content} |")
        
        # Prints border.
        print("+",  end="")
        for _ in range(len(self._content)):
            print("-",  end="")
        print("+")


        
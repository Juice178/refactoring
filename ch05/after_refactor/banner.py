from typing import Final


class Banner:
    def __init__(self, content: str) -> None:
        self._content: Final[str] = content

    def print(self, times: int) -> None:
        self.print_border()
        self.print_content(times)
        self.print_border()

    def print_border(self) -> None:
        print("+",  end="")
        for _ in range(len(self._content)):
            print("-",  end="")
        print("+")

    def print_content(self, times: int) -> None:
        for _ in range(times):
            print(f"| {self._content} |")

        
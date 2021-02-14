from label import Label
from typing import Optional

class Person:
    def __init__(self, name: Optional[Label], mail: Optional[Label]) -> None:
        self._name = name 
        self._mail = mail 

    def display(self) -> None:
        if self._name is not None:
            self._name.display()
        if self._mail is not None:
            self._mail.display()

    def __str__(self) -> str:
        result = "[ Person:"
        result += " name="
        if self._name is None:
            result += "(none)"
        else:
            result += f"{self._name}"
        result += " mail="
        if self._mail is None:
            result += "(none)"
        else:
            result += f"{self._mail}"
        result += " ]"
        return result
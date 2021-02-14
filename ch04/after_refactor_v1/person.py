from label import Label
from null_label import NullLabel


class Person:
    def __init__(self, name: Label = NullLabel(), mail: Label = NullLabel()) -> None:
        self._name = name 
        self._mail = mail 

    def display(self) -> None:
        self._name.display()
        self._mail.display()

    def __str__(self) -> str:
        return f"[ Person: name= {self._name} mail= {self._mail} ]"
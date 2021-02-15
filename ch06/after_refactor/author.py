class Author:
    def __init__(self, name: str, mail: str) -> None:
        self._name = name 
        self._mail = mail 

    def get_name(self) -> str:
        return self._name 

    def get_mail(self) -> str:
        return self._mail 

    def set_name(self, name: str) -> None:
        self._name = name 

    def set_mail(self, mail: str) -> None:
        self._mail = mail
from author import Author


class Book:
    def __init__(self, title: str, isbn: str, price: str, 
                 author_name: str, author_mail: str) -> None:
        self._title = title 
        self._isbn = isbn 
        self._price = price
        self._author = Author(author_name, author_mail)
        self._author_mail = author_mail

    def get_title(self) -> str:
        return self._title 

    def get_isbn(self) -> str:
        return self._isbn

    def get_price(self) -> str:
        return self._price 

    def get_author_name(self) -> str:
        return self._author.get_name()

    def get_author_mail(self) -> str:
        return self._author.get_mail()

    def set_author_name(self, name: str) -> None:
        self._author.set_name(name)

    def set_author_mail(self, mail: str) -> None:
        self._author.set_mail(mail)

    def to_xml(self):
        author = self.tag("author", self.tag("name", self._author.get_name()) + self.tag("mail", self._author.get_mail()))
        book = self.tag("book", self.tag("title", self._title) + self.tag("isbn", self._isbn) + self.tag("price",  self._price) + author)
        return book 

    def tag(self, element: str, content: str) -> str:
        return f"<{element}>{content}</{element}>\n"
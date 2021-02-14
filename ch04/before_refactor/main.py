from person import Person 
from label import Label


def main() -> None:
    people = [
        Person(Label("Alice"), Label("alice@example.com")), 
        Person(Label("Boby"), Label("boby@example.com")), 
        Person(Label("Chirs"), None)
    ]

    for p in people:
        print(p)
        p.display()
        print("")

if __name__ == '__main__':
    main()
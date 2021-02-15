from item import Item 
from item_type import ItemType

def main() -> None:
    book = Item(
        ItemType.BOOK, 
        "World History", 
        4800)

    dvd = Item(
        ItemType.DVD, 
        "DVD Volume1", 
        3000)

    soft = Item(
        ItemType.SOFTWARE, 
        "Emulator", 
        3200)

    print(f"book = {book}")
    print(f"div  = {dvd}")
    print(f"soft = {soft}")


if __name__ == '__main__':
    main()


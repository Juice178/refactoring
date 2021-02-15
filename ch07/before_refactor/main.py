from item import Item 


def main() -> None:
    book = Item(
        Item.TYPECODE_BOOK, 
        "World History", 
        4800)

    dvd = Item(
        Item.TYPECODE_DVD, 
        "DVD Volume1", 
        3000)

    soft = Item(
        Item.TYPECODE_SOFTWARE, 
        "Emulator", 
        3200)

    print(f"book = {book}")
    print(f"div  = {dvd}")
    print(f"soft = {soft}")


if __name__ == '__main__':
    main()


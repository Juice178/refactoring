from address_file import AddressFile


def main() -> None:
    file = AddressFile(filename="address.txt", section="address")
    file.set("Hiroshi Yuki", "hyuki@example.com")
    file.set("Tomura", "tomura@example.com")
    file.set("Hanako Sato", "hanako@example.com")
    file.update()

    names = file.names()
    for name in names:
        mail = file.get(name)
        print(f"name={name}, mail={mail}")
    

if __name__ == "__main__":
    main()




from address_file import AddressFile


def main() -> None:
    file = AddressFile(filename="address.txt", section="address")
    file.get_database().set("Hiroshi Yuki", "hyuki@example.com")
    file.get_database().set("Tomura", "tomura@example.com")
    file.get_database().set("Hanako Sato", "hanako@example.com")
    file.get_database().update()

    names = file.names()
    for name in names:
        mail = file.get_database().get(name)
        print(f"name={name}, mail={mail}")
    

if __name__ == "__main__":
    main()




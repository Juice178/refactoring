from simple_database import SimpleDatabase

def main():
    db = SimpleDatabase("dbfile.txt")
    it = db.iterator()
    while (key := next(it, None)) != None:
        print(f"KEY: {key}")
        print(f"VALUE: {db.get_value(key)}")


if __name__ == '__main__':
    main()
from book import Book

def main() -> None:
    refactoring = Book(
        "Refactoring: imporving the design of existing code", 
        "ISBN323232", 
        "$44.95", 
        "Martin Fowloer", 
        "follower@acm.org"
    )

    print("rafactoring: ")
    print(refactoring.to_xml())



if __name__ == '__main__':
    print("hi")
    main()